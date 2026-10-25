# Author:Yi Sun(Tim) 2023-08-29

"""Admin home page. Only depends on AdminLayout (no other concrete page is imported)."""
from selenium.webdriver.common.by import By
from pages.admin_layout import AdminLayout


class AdminPage(AdminLayout):
    """
        Note: For security and confidentiality, specific XPath/CSS selectors
        have been replaced with 'test_sample', and additional private locators
        have been omitted from this public sample.
    """
    SEARCH_BOXES = {
        "quote": (By.ID, "test_sample"),
        "address": (By.ID, "test_sample"),
        "client": (By.ID, "test_sample"),
    }

    def get_top_menu_texts(self) -> list:
        return [self.text_of(loc) for loc in (self.QUOTES_MENU, self.SERVICES_MENU,self.LISTS_MENU, self.ACCOUNT_MENU)]

    def is_search_box_displayed(self, kind: str) -> bool:
        return self.is_visible(self.SEARCH_BOXES[kind])

    def get_quotes_menu_items(self) -> list:
        self.open_quote_menu()
        return [self.text_of(loc) for loc in self.QUOTES_ITEMS]

    def get_services_menu_items(self) -> list:
        self.open_services_menu()
        return [self.text_of(loc) for loc in self.SERVICES_ITEMS]

    def get_list_menu_items(self) -> list:
        self.open_list_menu()
        return [self.text_of(loc) for loc in self.LIST_ITEMS]

    def get_account_menu_items(self) -> list:
        self.open_account_menu()
        return [self.text_of(loc) for loc in self.ACCOUNT_ITEMS]

