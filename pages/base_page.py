# Author:Yi Sun(Tim) 2023-08-29

"""BasePage: the only layer that talks to Selenium directly.
Page classes call these wrappers; tests never touch the driver."""
import logging
from typing import Tuple
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

Locator = Tuple[str, str]
log = logging.getLogger(__name__)


class BasePage:
    TIMEOUT = 20

    def __init__(self, driver, timeout: int = None):
        self.driver = driver
        self.timeout = timeout or self.TIMEOUT

    def _wait(self, timeout=None) -> WebDriverWait:
        return WebDriverWait(self.driver, timeout or self.timeout)

    # ---- finding ----
    def find(self, locator: Locator, timeout=None):
        return self._wait(timeout).until(EC.presence_of_element_located(locator),
                                         message=f"Element not present: {locator}")

    def find_visible(self, locator: Locator, timeout=None):
        return self._wait(timeout).until(EC.visibility_of_element_located(locator),
                                         message=f"Element not visible: {locator}")

    # ---- actions ----
    def click(self, locator: Locator, timeout=None) -> None:
        log.debug("click %s", locator)
        self._wait(timeout).until(EC.element_to_be_clickable(locator),
                                  message=f"Element not clickable: {locator}").click()

    def type_text(self, locator: Locator, text: str, clear: bool = True) -> None:
        log.debug("type into %s", locator)
        el = self.find_visible(locator)
        if clear:
            el.clear()
        el.send_keys(text)

    # ---- reading ----
    def text_of(self, locator: Locator, timeout=None) -> str:
        """Visible text with whitespace/nbsp collapsed ('Services      »' -> 'Services »')."""
        return " ".join(self.find_visible(locator, timeout).text.split())

    def is_visible(self, locator: Locator, timeout: int = 5) -> bool:
        try:
            self.find_visible(locator, timeout)
            return True
        except TimeoutException:
            return False

    def wait_for_text(self, locator: Locator, text: str, timeout=None) -> None:
        self._wait(timeout).until(EC.text_to_be_present_in_element(locator, text),
                                  message=f"Text '{text}' not shown in {locator}")

    @property
    def current_url(self) -> str:
        return self.driver.current_url

    def open(self, url: str) -> None:
        self.driver.get(url)

    # ---- <select> dropdowns ----
    def select_options(self, locator: Locator) -> list:
        """Texts of all options of a <select>."""
        return [option.text for option in Select(self.find(locator)).options]

    # 如果下拉框是隐藏 select，建议在基类里加一个通用方法
    def select_options_hidden(self, locator: Locator) -> list:
        """Texts of all options of a (possibly hidden) <select>."""
        return [o.get_attribute('textContent').strip()
                for o in Select(self.find(locator)).options]

    def selected_option(self, locator: Locator) -> str:
        """Text of the currently selected option of a <select>."""
        return Select(self.find(locator)).first_selected_option.text

    def select_by_text(self, locator: Locator, text: str) -> None:
        Select(self.find(locator)).select_by_visible_text(text)

    def select_combobox_option(self, input_id, text):
        toggle_loc = (
        By.XPATH, f"//input[@id='{input_id}']/following-sibling::a[contains(@class,'custom-combobox-toggle')]")
        self.click(toggle_loc)

        option_loc = (By.XPATH,
                      f"//input[@id='{input_id}']/parent::span/following-sibling::ul[contains(@class,'ui-autocomplete')][1]"
                      f"//li/a[normalize-space()='{text}']")
        self.click(option_loc)

    def select_by_index(self, locator: Locator, index: int) -> None:
        Select(self.find(locator)).select_by_index(index)

    # ---- scrolling / windows ----
    def scroll_to_bottom(self) -> None:
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def scroll_to_top(self) -> None:
        self.driver.execute_script("window.scrollTo(0, 0);")

    def switch_to_latest_window(self) -> None:
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def wait_until_invisible(self, locator, timeout=None) -> None:
        """Returns once the element is hidden or gone from the DOM."""
        self._wait(timeout).until(EC.invisibility_of_element_located(locator),
                                  message=f"Element still visible: {locator}")
