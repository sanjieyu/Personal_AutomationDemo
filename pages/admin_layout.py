# Author:Yi Sun(Tim) 2023-08-29

"""Shared layout of every page after login: top menu, menu items, footer.

Every concrete page (AdminPage, AccountCustomerPage, ...) inherits from this class.
RULE: this module must NOT import any concrete page - dependencies only point downwards.
"""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class AdminLayout(BasePage):
    """
        Note: For security and confidentiality, specific XPath/CSS selectors
        have been replaced with 'test_sample', and additional private locators
        have been omitted from this public sample.
    """
    # ---- top bar ----
    QUOTES_MENU = (By.ID, "test_sample")
    SERVICES_MENU = (By.XPATH, "test_sample")
    LISTS_MENU = (By.XPATH, "test_sample")
    ACCOUNT_CUSTOMER_MENU = (By.XPATH, "test_sample")
    REPORTS_MENU = (By.ID, "test_sample")
    ACCOUNT_MENU = (By.CSS_SELECTOR, "test_sample")

    # ---- footer ----
    COPYRIGHT = (By.XPATH, "test_sample")
    TERMS = (By.XPATH, "test_sample")

    # ---- Quotes menu (order == expected display order) ----
    QUOTES_ITEMS = [
        (By.XPATH, "test_sample"),
        (By.XPATH, "test_sample"),
    ]

    # ---- Quotes menu (order == expected display order) ----
    SERVICES_ITEMS = [
        (By.XPATH, "test_sample"),
        (By.XPATH, "test_sample"),
        (By.XPATH, "test_sample"),
    ]

    # ---- List menu ----
    # ACCOUNT_LIST_ITEM = (By.XPATH, "//a[normalize-space()='Account Customers']")
    LIST_ITEMS = [
        (By.XPATH, "test_sample"),
        (By.XPATH, "test_sample"),
        # ACCOUNT_LIST_ITEM,
        (By.XPATH, "test_sample"),
        (By.XPATH, "test_sample"),
        (By.XPATH, "test_sample"),
        (By.XPATH, "test_sample"),
        (By.XPATH, "test_sample"),
        (By.XPATH, "test_sample"),
        (By.XPATH, "test_sample"),
    ]

    # ---- Account menu ----
    ACCOUNT_ITEMS = [
        (By.XPATH, "test_sample"),
        (By.XPATH, "test_sample"),
        (By.XPATH, "test_sample"),
        (By.XPATH, "//a[test_sample='Users Management']"),
        (By.XPATH, "//a[test_sample='Travel Area Management']"),
        (By.CSS_SELECTOR, "test_sample"),
        (By.XPATH, "//a[test_sample='SMS Notifications']"),
        (By.XPATH, "//a[test_sample='Log off']"),
    ]

    def wait_until_loaded(self):
        """Default: the layout is loaded when the footer is visible. Pages may override."""
        self.find_visible(self.COPYRIGHT, timeout=30)
        return self

    # ---- shared actions ----
    def open_quote_menu(self) -> None:
        self.click(self.QUOTES_MENU)


    def open_services_menu(self) -> None:
        self.click(self.SERVICES_MENU)

    def open_list_menu(self) -> None:
        self.click(self.LISTS_MENU)

    def open_account_menu(self) -> None:
        self.click(self.ACCOUNT_MENU)

    def get_footer_texts(self) -> list:
        return [self.text_of(self.COPYRIGHT), self.text_of(self.TERMS)]
