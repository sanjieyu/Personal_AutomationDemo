# Author:Yi Sun(Tim) 2023-9-16

'''Add a Custom Door'''

from selenium.webdriver.common.by import By
from pages.custom_door_page import Custom_Door

class Add_Custom_Door(Custom_Door):
    """
        Note: For security and confidentiality, specific XPath/CSS selectors
        have been replaced with 'test_sample', and additional private locators
        have been omitted from this public sample.
    """
    new_door_page_loc = (By.ID,"test_sample")
    new_door_title= (By.ID,"test_sample")
    new_door_duplicate = (By.CSS_SELECTOR, "test_sample")
    new_door_delete = (By.CSS_SELECTOR, "test_sample")

    '''loc for validation'''
    validation_msgbox_loc = (By.ID,"test_sample")

    '''Check the input validateiong'''
    def validation_input(self)-> str:
        self.scroll_to_bottom()
        self.click(self.add_btn_loc)
        return self.text_of(self.validation_msgbox_loc)

    '''Input the necesary details for a door'''
    def add_custom_detail(self):
        self.select_by_text(self.install_type_select,'Residential')
        self.select_by_text(self.design_select,'Aliwood')
        self.select_by_text(self.colour_category_select,'OilColour')
        self.type_text(self.opensize_lh_select,'2800')
        self.type_text(self.opensize_rh_select, '2800')
        self.type_text(self.opensize_width_select, '5510')
        self.type_text(self.sr_left_select, '200')
        self.type_text(self.hr_select, '400')
        self.type_text(self.sr_right_select, '200')
        self.select_combobox_option(self.panel_wide_input_loc, '1 Panel Wide')
        self.select_by_text(self.opener_select, 'Lock Only')
        self.scroll_to_bottom()
        self.click(self.add_btn_loc)

    def new_added_custom_door(self)-> str:
        return self.text_of(self.new_door_title)

    def duplicate_btn(self) -> bool:
        return self.is_visible(self.new_door_duplicate)

    def delete_btn(self) -> bool:
        return self.is_visible(self.new_door_delete)

if __name__ == '__main__':
    # Debug run: right-click > Run in PyCharm, or:  python -m UIModule.add_quote_page
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

        Custom_Door(driver).add_quote()
        Custom_Door(driver).open_custom_door()
        page = Add_Custom_Door(driver)
        print(page.current_url)
        print(page.validation_input())
        page.add_custom_detail()
        print(page.new_added_custom_door())
        print(page.duplicate_btn())
        print(page.delete_btn())
    finally:
        driver.quit()
