# Author:Yi Sun(Tim) 2023-08-05

'''Test Account Customer Page'''

from pages.account_customer_page import AccountCustomerPage
from pages.admin_page import AdminPage
from tests.ui.base_test import BaseUITest


class AccountCustomerUITest(BaseUITest):
    RESET_EACH_TEST = False          # navigate once per class, like the old setUpClass style

    @classmethod
    def setUpClass(cls):
        super().setUpClass()                                   # reuse the shared, logged-in browser
        cls.driver.get(cls.base_url)
        AdminPage(cls.driver).wait_until_loaded()
        cls.account_page = AccountCustomerPage(cls.driver).go_to()

    def test_account_customer_ui_001(self):
        '''Verify the url'''
        self.assertEqual(self.base_url + 'Customer/Test', self.account_page.current_url)

    def test_account_customer_ui_002(self):
        '''Verify the title'''
        self.assertEqual('Account Customers', self.account_page.get_title())

    def test_account_customer_ui_003(self):
        '''Verify the search button'''
        self.assertTrue(self.account_page.is_search_button_displayed())

    def test_account_customer_ui_004(self):
        '''Verify the search box'''
        self.assertTrue(self.account_page.is_search_box_displayed())

    def test_account_customer_ui_005(self):
        '''Verify each column on this screen'''
        self.assertEqual(['Test Sample 1','Test Sample 2','Test Sample 3'],
                         self.account_page.get_column_headers())

    def test_account_customer_ui_006(self):
        '''Verify the Search function (changes the page, so keep it last: tests run in name order)'''
        self.assertEqual('yisun with test items', self.account_page.search_and_get_first_result('yi_sun'))


if __name__ == '__main__':
    unittest.main(verbosity=2)

