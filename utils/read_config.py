# Author:Yi Sun(Tim) 2022-09-13

"""Config reader. Env vars override config.ini so secrets never need to be committed."""
import configparser
import os
from collections import namedtuple
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent          # independent of the cwd
CONFIG_PATH = ROOT_DIR / "Config" / "config.ini"

Credentials = namedtuple("Credentials", "username password")
MailSettings = namedtuple("MailSettings", "host port user password sender receivers")


class ReadConfig:
    def __init__(self, path: Path = CONFIG_PATH):
        # interpolation=None: passwords may contain '%'
        self._cf = configparser.ConfigParser(interpolation=None)
        self._cf.read(path, encoding="utf-8")

    def _get(self, section: str, option: str, env_name: str) -> str:
        value = os.getenv(env_name) or self._cf.get(section, option, fallback="")
        if not value:
            raise KeyError(f"Missing [{section}] {option}; set it in config.ini or env var {env_name}")
        return value

    def get_url(self) -> str:
        return self._get("config", "url", "EGD_URL")

    def get_credentials(self, role: str) -> Credentials:
        """role: admin / dealer / sales"""
        prefix = f"EGD_{role.upper()}"
        return Credentials(
            self._get(role, "username", f"{prefix}_USERNAME"),
            self._get(role, "password", f"{prefix}_PASSWORD"),
        )

    def get_mail_settings(self) -> MailSettings:
        """[mail] section of config.ini; env vars SMTP_* / MAIL_* take priority if set."""
        user = self._get("mail", "smtp_user", "SMTP_USER")
        password = self._get("mail", "smtp_password", "SMTP_PASSWORD")
        receivers = [r.strip() for r in self._get("mail", "mail_to", "MAIL_TO").split(",") if r.strip()]
        host = os.getenv("SMTP_HOST") or self._cf.get("mail", "smtp_host", fallback="smtp.gmail.com")
        port = int(os.getenv("SMTP_PORT") or self._cf.get("mail", "smtp_port", fallback="587"))
        sender = os.getenv("MAIL_FROM") or self._cf.get("mail", "mail_from", fallback="") or user
        return MailSettings(host, port, user, password, sender, receivers)

    # ---- thin wrappers kept for APITest / legacy callers ----
    def admin_username(self): return self.get_credentials("admin").username
    def admin_password(self): return self.get_credentials("admin").password
    def dealer_username(self): return self.get_credentials("dealer").username
    def dealer_password(self): return self.get_credentials("dealer").password
    def sales_username(self): return self.get_credentials("sales").username
    def sales_password(self): return self.get_credentials("sales").password






