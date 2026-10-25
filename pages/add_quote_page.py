# Author:Yi Sun(Tim) 2023-09-04

'''Add Quote Page'''

from selenium.webdriver.common.by import By
from pages.admin_layout import AdminLayout

DEFAULT_ACCOUNT_CUSTOMER = "For Automation Testing"


class Add_Quote(AdminLayout):
    """
        Note: For security and confidentiality, specific XPath/CSS selectors
        have been replaced with 'test_sample', and additional private locators
        have been omitted from this public sample.
    """
    main_page_loc1 = (By.XPATH,"test_sample")
    main_page_loc = (By.XPATH,"test_sample")

    '''loc for each section in this page'''
    proposal_details_loc = (By.CSS_SELECTOR, "test_sample")
    contact_details_loc = (By.XPATH, "test_sample")
    site_details_loc = (By.XPATH, "test_sample")
    doors_loc = (By.XPATH, "test_sample")
    add_door_btn = (By.CSS_SELECTOR, "test_sample")
    save_quote_btn = (By.ID, "test_sample")
    proceed_quote_btn = (By.ID, "test_sample")

    '''Quote Sucessfully modified popup'''
    proceed_ok_btn_loc = (By.XPATH,"test_sample")
    save_ok_btn_loc = (By.XPATH, "test_sample")

    '''loc for each element in "Proposal Details" section'''
    proposal_num_loc = (By.CSS_SELECTOR,"test_sample")
    pricing_cate_loc = (By.CSS_SELECTOR,"test_sample")
    user_quote_loc = (By.CSS_SELECTOR,"test_sample")
    account_type_loc = (By.CSS_SELECTOR,"test_sample")
    order_date_loc = (By.CSS_SELECTOR,"test_sample")
    quote_status_loc = (By.CSS_SELECTOR,"test_sample")
    cash_sale_account_loc = (By.CSS_SELECTOR,"test_sample")
    supply_type_loc = (By.CSS_SELECTOR,"test_sample")
    proplsal_num_box = (By.ID,"test_sample")
    pricing_cate_select = (By.ID,"test_sample")
    user_quote_select = (By.ID,"test_sample")
    account_type_select = (By.ID,"test_sample")
    order_date_select = (By.ID,"test_sample")
    quote_status_select = (By.ID,"test_sample")
    account_customer_btn = (By.CSS_SELECTOR, "test_sample")
    propertygroup_customer_loc = (By.LINK_TEXT,'For Automation Testing')
    cash_sales_account_select_loc = (By.ID,"test_sample")
    cash_sales_account_btn_loc = (By.CSS_SELECTOR, "test_sample")
    cash_sales_reswholesale_loc = (By.XPATH, "test_sample")
    account_customer_select1 = (By.ID,"test_sample")
    account_customer_select = (By.XPATH,"test_sample")
    supply_type_select = (By.ID,"test_sample")
    account_customer_loc = (By.XPATH,"test_sample")

    '''loc for each element in "Client Contact Details" section'''
    client_contact_details_loc = (By.XPATH, "test_sample")
    client_name_loc = (By.CSS_SELECTOR, "test_sample")
    customer_purchase_order_loc = (By.CSS_SELECTOR, "test_sample")
    contact_name_loc = (By.CSS_SELECTOR, "test_sample")
    contact_mobile_loc = (By.CSS_SELECTOR, "test_sample")
    contact_email_loc = (By.CSS_SELECTOR, "test_sample")
    contact_address_loc = (By.CSS_SELECTOR, "test_sample")
    contact_suburb_loc = (By.CSS_SELECTOR, "test_sample")
    contact_postcode_loc = (By.CSS_SELECTOR, "test_sample")
    client_name_box = (By.ID,"test_sample")
    order_num_box = (By.ID,"test_sample")
    contact_name_box = (By.ID,"test_sample")
    contact_mobile_box = (By.ID,"test_sample")
    contact_email_box = (By.ID,"test_sample")
    contact_address_box = (By.ID,"test_sample")
    contact_suburb_box = (By.ID,"test_sample")
    contact_postcode_box = (By.ID,"test_sample")
    CLIENT_FIELDS = {  # field name used by is_client_field_displayed()
        "client_name": client_name_box, "order_num": order_num_box, "contact_name": contact_name_box,
        "contact_mobile": contact_mobile_box, "contact_email": contact_email_box,
        "contact_address": contact_address_box, "contact_suburb": contact_suburb_box,
        "contact_postcode": contact_postcode_box,
    }


    '''loc for each element in "Site Contact Details" section'''
    site_contact_details_loc = (By.XPATH, "test_sample")
    copy_client_details_loc = (By.XPATH, "test_sample")
    site_contact_name = (By.CSS_SELECTOR, "test_sample")
    site_phone_loc = (By.CSS_SELECTOR, "test_sample")
    site_email_loc = (By.CSS_SELECTOR, "test_sample")
    site_address_loc = (By.CSS_SELECTOR, "test_sample")
    site_suburb_loc = (By.CSS_SELECTOR, "test_sample")
    site_postcode_loc = (By.CSS_SELECTOR, "test_sample")
    copy_checkbox_loc = (By.ID,"test_sample")
    site_contactname_box = (By.ID,"test_sample")
    site_phone_box = (By.ID,"test_sample")
    site_email_box = (By.ID,"test_sample")
    site_address_box = (By.ID,"test_sample")
    site_suburb_box = (By.ID,"test_sample")
    site_postcode_box = (By.ID,"test_sample")
    SITE_FIELDS = {  # field name used by is_site_field_displayed()
        "contact_name": site_contactname_box, "phone": site_phone_box, "email": site_email_box,
        "address": site_address_box, "suburb": site_suburb_box, "postcode": site_postcode_box,
    }

    '''loc for Copy Client address checkbox'''
    copy_client_address_loc = (By.XPATH,"test_sample")
    copy_client_address_checkbox_loc = (By.ID,"test_sample")

    '''loc for Doors'''
    add_door_menu = (By.XPATH,""test_sample")

    '''loc for Valication page'''
    validation_error_loc = (By.XPATH,"test_sample")
    validation_1_loc = (By.XPATH, "test_sample")
    validation_2_loc = (By.XPATH,"test_sample")
    validation_ok_btn = (By.ID,"test_sample")
    errors_modal_loc = (By.ID, "test_sample")
    modal_backdrop_loc = (By.CSS_SELECTOR, "test_sample")

    '''loc for add successfully'''
    quote_success_created_loc = (By.XPATH, "test_sample")
    success_btn_loc = (By.XPATH,"test_sample")

    # ================= navigation =================
    def add_quote(self) -> "Add_Quote":
        """Add menu > Quote (replaces go_addquote)."""
        self.open_quote_menu()
        self.click(AdminLayout.QUOTES_ITEMS[0])
        return self.wait_until_loaded()

    def wait_until_loaded(self) -> "Add_Quote":
        self.find_visible(self.contact_details_loc, timeout=20)
        return self

    # ================= reads =================
    def get_default_sections(self) -> list:
        return [self.text_of(loc) for loc in (self.proposal_details_loc, self.contact_details_loc,
                                              self.site_details_loc, self.doors_loc)]

    def is_save_quote_button_displayed(self) -> bool:
        return self.is_visible(self.save_quote_btn)

    def check_proposal_details(self) -> list:
        return [self.text_of(loc) for loc in (
            self.proposal_num_loc, self.pricing_cate_loc, self.user_quote_loc, self.account_type_loc,
            self.order_date_loc, self.quote_status_loc, self.cash_sale_account_loc, self.supply_type_loc)]

    def check_pricing_cate_value(self) -> list:
        return self.select_options(self.pricing_cate_select)

    def check_default_pricing(self) -> str:
        return self.selected_option(self.pricing_cate_select)

    def check_default_user(self) -> str:
        return self.selected_option(self.user_quote_select)

    def check_accounttype_value(self) -> list:
        return self.select_options(self.account_type_select)

    def check_default_accounttype(self) -> str:
        return self.selected_option(self.account_type_select)

    def check_quotestatus_value(self) -> list:
        return self.select_options(self.quote_status_select)

    def get_selected_quote_status(self) -> str:
        return self.selected_option(self.quote_status_select)

    def is_account_customer_enabled(self) -> bool:
        """True when the 'Account Customer' list is NOT disabled."""
        return not self.find(self.account_customer_select, timeout=10).get_attribute("disabled")

    def check_supplytype_value(self) -> list:
        return self.select_options(self.supply_type_select)

    def check_supplytype_default(self) -> str:
        return self.selected_option(self.supply_type_select)

    def check_changeto_Account(self) -> bool:
        """True when the 'Account Customer' list is NOT disabled."""
        return not self.find(self.account_customer_select, timeout=10).get_attribute("disabled")

    def get_account_customer_label(self) -> str:
        return self.text_of(self.account_customer_loc)

    def check_contact_details(self) -> list:
        return [self.text_of(loc) for loc in (self.client_contact_details_loc, self.site_contact_details_loc,
                                              self.copy_client_details_loc)]

    def check_copy_client_address(self) -> str:
        return self.text_of(self.copy_client_address_loc)

    def check_client_contact_details(self) -> list:
        return [self.text_of(loc) for loc in (
            self.client_name_loc, self.customer_purchase_order_loc, self.contact_name_loc,
            self.contact_mobile_loc, self.contact_email_loc, self.contact_address_loc,
            self.contact_suburb_loc, self.contact_postcode_loc)]

    def is_client_field_displayed(self, field: str) -> bool:
        """field: client_name / order_num / contact_name / contact_mobile / contact_email /
        contact_address / contact_suburb / contact_postcode"""
        return self.is_visible(self.CLIENT_FIELDS[field])

    def check_site_contact_details(self) -> list:
        return [self.text_of(loc) for loc in (
            self.site_contact_name, self.site_phone_loc, self.site_email_loc,
            self.site_address_loc, self.site_suburb_loc, self.site_postcode_loc)]

    def check_copy_checkbox(self) -> bool:
        return self.find(self.copy_checkbox_loc).is_selected()

    def is_site_field_displayed(self, field: str) -> bool:
        """field: contact_name / phone / email / address / suburb / postcode"""
        return self.is_visible(self.SITE_FIELDS[field])

    def check_adddoor_btn(self) -> str:
        return self.text_of(self.add_door_btn)

    def check_adddoor_menu(self) -> list:
        """Open the 'Add door' dropdown and return its item texts (one per line)."""
        self.scroll_to_bottom()
        self.click(self.add_door_btn)
        text = self.find_visible(self.add_door_menu).text
        return [line.strip() for line in text.splitlines() if line.strip()]

    # ================= actions =================
    def select_account_type(self, text: str) -> None:
        self.select_by_text(self.account_type_select, text)

    def select_supply_type_by_index(self, index: int) -> None:
        self.select_by_index(self.supply_type_select, index)

    def save_quote(self) -> None:
        self.scroll_to_bottom()
        self.click(self.save_quote_btn)

    def check_validation(self) -> list:
        """Click Save on an incomplete quote, read the validation popup, close it.
        Returns [title, message 1, message 2]."""
        self.click(self.save_quote_btn)
        self.switch_to_latest_window()
        self.find_visible(self.validation_error_loc, timeout=10)
        texts = [self.text_of(loc) for loc in (self.validation_error_loc, self.validation_1_loc,
                                               self.validation_2_loc)]
        self.click(self.validation_ok_btn)
        self.wait_until_invisible(self.errors_modal_loc)   # handle pop up
        self.wait_until_invisible(self.modal_backdrop_loc)
        return texts

    def check_add_quote_success(self, email: str, customer: str = DEFAULT_ACCOUNT_CUSTOMER) -> str:
        """Fill the minimum fields for an 'Account' quote, save, return the success message."""
        self.select_supply_type_by_index(1)
        self.type_text(self.contact_email_box, email)
        self.select_account_type("Account")
        self.click(self.account_customer_btn)
        self.click((By.LINK_TEXT, customer))
        self.save_quote()
        self.scroll_to_top()
        self.find_visible(self.quote_success_created_loc, timeout=15)
        return self.text_of(self.quote_success_created_loc)

    def create_cash_sale_quote_and_proceed(self, email: str, client_name: str = "Add by Automation",
                                           contact_name: str = "Add by Automation",
                                           mobile: str = "040000000") -> None:
        """Replaces change_quote_detail: Cash sale quote -> Save -> Proceed (used before adding doors)."""
        self.select_supply_type_by_index(2)
        self.select_account_type("Cash sale")
        self.click(self.cash_sales_account_btn_loc)
        self.click(self.cash_sales_reswholesale_loc)
        self.type_text(self.client_name_box, client_name)
        self.type_text(self.contact_name_box, contact_name)
        self.type_text(self.contact_mobile_box, mobile)
        self.type_text(self.contact_email_box, email)
        self.save_quote()
        self.find_visible(self.quote_success_created_loc, timeout=15)
        self.click(self.proceed_quote_btn)

    def check_account_customer(self)-> str:
        '''Switch from Default Cash sale to Account Customer, check the account cusomter dropdown'''
        self.select_account_type("Account")
        return self.text_of(self.account_customer_loc)

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

        page = Add_Quote(driver).add_quote()
        print(page.current_url)
        print(page.get_default_sections())
        print(page.get_supply_type_options())
    finally:
        driver.quit()






