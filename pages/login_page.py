# Author:Yi Sun(Tim) 2023-08-29

"""Login page."""
"""Login page. Knows nothing about what comes after login (admin / dealer / sales home pages differ)."""
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from UIModule.base_page import BasePage


class LoginPage(BasePage):
    USERNAME = (By.ID, "Email")
    PASSWORD = (By.ID, "Password")
    # TODO: replace the positional XPath with a stable locator (e.g. input[type='submit']) once verified
    LOGIN_BTN = (By.XPATH, '//*[@id="loginForm"]/form/div[4]/div/input')

    def login(self, username: str, password: str) -> None:
        """Submit the credentials and wait until the login form is gone.
        The caller decides which page to check next, e.g. AdminPage(driver).wait_until_loaded()."""
        self.type_text(self.USERNAME, username)
        self.type_text(self.PASSWORD, password)
        self.click(self.LOGIN_BTN)
        self._wait(30).until(EC.invisibility_of_element_located(self.USERNAME),
                             message="Login form is still displayed - login failed?")
