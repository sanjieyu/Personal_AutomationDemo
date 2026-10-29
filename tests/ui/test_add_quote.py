# Author:Yi Sun(Tim) 2023-09-04

'''Test Add Quote Page'''

from pages.add_quote_page import Add_Quote
from pages.admin_page import AdminPage
from tests.ui.base_test import BaseUITest

class AddQuoteUITest(BaseUITest):
    RESET_EACH_TEST = False

    @classmethod
    def setUpClass(cls):
        super().setUpClass()                                   # reuse the shared, logged-in browser
        cls.driver.get(cls.base_url)
        AdminPage(cls.driver).wait_until_loaded()
        cls.add_quote_page = Add_Quote(cls.driver).add_quote()


    def test_addquote_ui_001(self):
        '''Verify the url for Add Quotes page'''
        self.assertEqual(self.base_url + 'Quote/Sample', self.add_quote_page.current_url)

    def test_addquote_ui_002(self):
        '''Verify the default section in Add Quotes page'''
        self.assertEqual(['Test Sample 1','Test Sample 2','Test Sample 3'],self.add_quote_page.get_default_sections())

    def test_addquote_ui_003(self):
        '''Verify the Save Quote button in Add Quotes page'''
        self.driver.implicitly_wait(2)
        self.assertTrue(self.add_quote_page.is_save_quote_button_displayed())


    def test_addquote_ui_004(self):
        '''Verify each description of Proplsal Details in Add Quotes page'''
        self.assertEqual(['Test Sample 1','Test Sample 2','Test Sample 3'],self.add_quote_page.check_proposal_details())

    def test_addquote_ui_005(self):
        '''Verify each value in "Pricing Category" list'''
        self.assertEqual(['Test Sample 1','Test Sample 2','Test Sample 3'],
                         self.add_quote_page.check_pricing_cate_value())

    def test_addquote_ui_006(self):
        '''Verify the default value in "Pricing Category" list'''
        self.assertEqual(('Test Sample 4'),self.add_quote_page.check_default_pricing())

    def test_addquote_ui_007(self):
        '''Verify the default value in "User" list'''
        self.assertEqual(('Yi Sun'),self.add_quote_page.check_default_user())

    def test_addquote_ui_008(self):
        '''Verify each value in "Account Type" list'''
        self.assertEqual(['Test Sample 1','Test Sample 2','Test Sample 3'],
                         self.add_quote_page.check_accounttype_value())

    def test_addquote_ui_009(self):
        '''Verify the default value in "Account Type" list'''
        self.assertEqual(('Test Sample'),self.add_quote_page.check_default_accounttype())

    def test_addquote_ui_010(self):
        '''Verify each value in "Quote Status" list'''
        self.assertEqual(['Test Sample 1','Test Sample 2'],self.add_quote_page.check_quotestatus_value())

    def test_addquote_ui_011(self):
        '''Verify the default value in "Quote Status" list, it should be "Quote"'''
        self.assertEqual(('Test Sample'),self.add_quote_page.check_default_accounttype())

    def test_addquote_ui_012(self):
        '''Verify each value in "Supply Type" list'''
        self.assertEqual(['Test Sample 1','Test Sample 2','Test Sample 3'],self.add_quote_page.check_supplytype_value())

    def test_addquote_ui_013(self):
        '''Verify the default value in "Supply Type" list'''
        self.assertEqual('Please Select',self.add_quote_page.check_supplytype_default())
    def test_addquote_ui_014(self):
        '''Verify The "Account Customer" list should enable after select "Account" in "Account Type" list'''
        self.assertTrue(self.add_quote_page.check_changeto_Account())

    def test_addquote_ui_015(self):
        '''Verify each section in "Contact Details"'''
        self.assertEqual(['Test Sample 1','Test Sample 2','Test Sample 3'],self.add_quote_page.check_contact_details())

    def test_addquote_ui_016(self):
        '''Verify each element in "Client Contact Details"'''
        self.driver.implicitly_wait(2)
        self.assertEqual( ['Test Sample 1','Test Sample 2','Test Sample 3'],self.add_quote_page.check_client_contact_details())

    def test_addquote_ui_017(self):
        '''Verify  the input editbox for "Client Name"'''
        self.assertTrue(self.add_quote_page.is_client_field_displayed("client_name"))

    def test_addquote_ui_018(self):
        '''Verify  the input editbox for "Customer Purchase Order"'''
        self.assertTrue(self.add_quote_page.is_client_field_displayed("order_num"))
    #
    def test_addquote_ui_019(self):
            '''Verify  the input editbox for "Contact Name"'''
            self.assertTrue(self.add_quote_page.is_client_field_displayed("contact_name"))

    def test_addquote_ui_020(self):
            '''Verify  the input editbox for "Contact Mobile"'''
            self.assertTrue(self.add_quote_page.is_client_field_displayed("contact_mobile"))

    def test_addquote_ui_021(self):
            '''Verify  the input editbox for "Contact Email"'''
            self.assertTrue(self.add_quote_page.is_client_field_displayed("contact_email"))

    def test_addquote_ui_022(self):
        '''Verify  the input editbox for "Contact Address"'''
        self.assertTrue(self.add_quote_page.is_client_field_displayed("contact_address"))

    def test_addquote_ui_023(self):
            '''Verify  the input editbox for "Contact Suburb"'''
            self.assertTrue(self.add_quote_page.is_client_field_displayed("contact_suburb"))

    def test_addquote_ui_024(self):
            '''Verify  the input editbox for "Contact Postcode"'''
            self.assertTrue(self.add_quote_page.is_client_field_displayed("contact_postcode"))

    def test_addquote_ui_025(self):
        '''Verify each element in "Site Contact Details"'''
        self.assertEqual( ['Test Sample 1','Test Sample 2','Test Sample 3'],
                          self.add_quote_page.check_site_contact_details())
    def test_addquote_ui_026(self):
            '''Verify the default status for checkbox for "Copy Client details"'''
            self.assertFalse( self.add_quote_page.check_copy_checkbox())

    def test_addquote_ui_027(self):
            '''Verify  the input editbox for "Site Contact Name"'''
            self.assertTrue( self.add_quote_page.is_site_field_displayed("contact_name"))

    def test_addquote_ui_028(self):
        '''Verify  the input editbox for "Site Phone"'''
        self.assertTrue( self.add_quote_page.is_site_field_displayed("phone"))

    def test_addquote_ui_029(self):
            '''Verify  the input editbox for "Site Email"'''
            self.assertTrue( self.add_quote_page.is_site_field_displayed("email"))

    def test_addquote_ui_030(self):
            '''Verify  the input editbox for "Site Address"'''
            self.assertTrue( self.add_quote_page.is_site_field_displayed("address"))

    def test_addquote_ui_031(self):
            '''Verify  the input editbox for "Site Suburb"'''
            self.assertTrue( self.add_quote_page.is_site_field_displayed("suburb"))

    def test_addquote_ui_032(self):
            '''Verify  the input editbox for "Site Postcode"'''
            self.assertTrue( self.add_quote_page.is_site_field_displayed("postcode"))
    #
    def test_addquote_ui_033(self):
            '''Verify  the "Add New Door" button"'''
            self.assertEqual( 'Add New Door',self.add_quote_page.check_adddoor_btn())

    def test_addquote_ui_034(self):
            '''Verify the add new door menu'''
            self.driver.refresh()
            self.assertEqual(['Test Sample 1','Test Sample 2'],self.add_quote_page.check_adddoor_menu())
    def test_addquote_ui_035(self):
            '''Verify the validation in Add Quote page'''
            self.assertEqual(['Test Sample 1','Test Sample 2','Test Sample 3'],self.add_quote_page.check_validation())

    def test_addquote_ui_036(self):
        '''Verify Add a Quote Successfully'''
        self.assertEqual(('(Test Sample successfully created)'),self.add_quote_page.check_add_quote_success('test@sample'))

    def test_addquote_ui_037(self):
        '''Verify Switch from Default Cash sale to Account Customer, check the account cusomter dropdown'''
        self.assertEqual(('Test Sample'),self.add_quote_page.check_account_customer())

    def test_addquote_ui_038(self):
        '''Verify "copy client address"'''
        self.assertEqual(('Test Sample'),self.add_quote_page.check_copy_client_address())

if __name__ == '__main__':
    unittest.main(verbosity=2)

