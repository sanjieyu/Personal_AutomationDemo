# Author:Yi Sun(Tim) 2023-08-05


"""Account Customer list page. Depends on AdminLayout (shared menu) - never the other way round."""
from selenium.webdriver.common.by import By
from pages.admin_layout import AdminLayout


class AccountCustomerPage(AdminLayout):
    """
        Note: For security and confidentiality, specific XPath/CSS selectors
        have been replaced with 'test_sample', and additional private locators
        have been omitted from this public sample.
    """
    TITLE = (By.CSS_SELECTOR, "test_sample")
    SEARCH_BTN = (By.CSS_SELECTOR, "test_sample")
    SEARCH_BOX = (By.ID, "test_sample")
    COLUMNS = [(By.XPATH, f"//span[text()='{name}']")
               for name in ("ID", "Account Customer", "Status", "City", "State", "Terms")]
    RESULT_LINK = (By.XPATH, "test_sample")

    def go_to(self) -> "AccountCustomerPage":
        """Open this page from the top menu (like the old goto_account_customer)."""
        self.click(self.ACCOUNT_CUSTOMER_MENU)
        return self.wait_until_loaded()

    def wait_until_loaded(self) -> "AccountCustomerPage":    # overrides the layout default
        self.find_visible(self.TITLE, timeout=60)
        return self

    def get_title(self) -> str:
        return self.text_of(self.TITLE)

    def is_search_button_displayed(self) -> bool:
        return self.is_visible(self.SEARCH_BTN)

    def is_search_box_displayed(self) -> bool:
        return self.is_visible(self.SEARCH_BOX)

    def get_column_headers(self) -> list:
        return [self.text_of(loc) for loc in self.COLUMNS]

    def search_and_get_first_result(self, keyword: str) -> str:
        self.type_text(self.SEARCH_BOX, keyword)
        self.click(self.SEARCH_BTN)
        self.wait_for_text(self.RESULT_LINK, keyword)
        return self.text_of(self.RESULT_LINK)

if __name__ == '__main__':
    from selenium import webdriver
    from CommonModule.read_config import ReadConfig
    from UIModule.login_page import LoginPage

    config = ReadConfig()
    creds = config.get_credentials("admin")

    driver = webdriver.Firefox()
    driver.maximize_window()
    try:
        driver.get(config.get_url())
        LoginPage(driver).login(creds.username, creds.password)

        page = AccountCustomerPage(driver).go_to()
        print(page.get_title())
        print(page.get_column_headers())
        print(page.search_and_get_first_result("test_sample"))
    finally:
        driver.quit()