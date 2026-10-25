# Author:Yi Sun(Tim) 2023-08-29

"""Shared base class for UI tests.

- ONE browser + ONE admin login for the whole test run (opened on first use, closed at exit via atexit).
  setUpClass only *reuses* that browser; it does not open a new one.
- RESET_EACH_TEST = True  : every test starts from a fresh admin home page (safest, a bit slower)
  RESET_EACH_TEST = False  : the test class prepares the page once in its own setUpClass (fastest, like your old style)
- a screenshot is saved automatically for every failed/errored test
"""
import atexit
import logging
import os
import re
import unittest
from datetime import datetime

from CommonModule.driver_factory import create_driver
from CommonModule.read_config import ROOT_DIR, ReadConfig
from UIModule.admin_page import AdminPage
from UIModule.login_page import LoginPage

log = logging.getLogger(__name__)
SCREENSHOT_DIR = ROOT_DIR / "Report" / "UI" / "screenshots"

_driver = None


def get_base_url() -> str:
    return (os.getenv("EGD_URL") or ReadConfig().get_url()).rstrip("/") + "/"


def _quit_driver() -> None:
    global _driver
    if _driver is not None:
        try:
            _driver.quit()
        finally:
            _driver = None


def get_admin_driver():
    """Create the browser and log in as admin on first use only."""
    global _driver
    if _driver is None:
        driver = create_driver(os.getenv("EGD_BROWSER", "firefox"), os.getenv("EGD_HEADLESS") == "1")
        atexit.register(_quit_driver)
        _driver = driver
        try:
            creds = ReadConfig().get_credentials("admin")
            driver.get(get_base_url())
            LoginPage(driver).login(creds.username, creds.password)
        except Exception:
            _quit_driver()          # do not leave a half-logged-in browser for the next class
            raise
    return _driver


class BaseUITest(unittest.TestCase):
    RESET_EACH_TEST = True
    driver = None
    base_url = None

    @classmethod
    def setUpClass(cls):
        cls.driver = get_admin_driver()      # reuses the already-open browser
        cls.base_url = get_base_url()

    def setUp(self):
        if self.RESET_EACH_TEST:
            self.driver.get(self.base_url)
            self.admin_page = AdminPage(self.driver).wait_until_loaded()

    # ---- failure screenshot ----
    def run(self, result=None):
        before = (len(getattr(result, "failures", [])), len(getattr(result, "errors", [])))
        outcome = super().run(result)
        after = (len(getattr(result, "failures", [])), len(getattr(result, "errors", [])))
        if result is not None and after != before:
            self._save_screenshot()
        return outcome

    def _save_screenshot(self) -> None:
        if self.driver is None:
            return
        try:
            SCREENSHOT_DIR.mkdir(parents=True, exist_ok=True)
            name = re.sub(r"[^\w.-]+", "_", self.id())[-120:]
            path = SCREENSHOT_DIR / f"{name}_{datetime.now():%H%M%S}.png"
            self.driver.save_screenshot(str(path))
            log.error("Failure screenshot: %s", path)
        except Exception:
            log.exception("Could not capture screenshot")
