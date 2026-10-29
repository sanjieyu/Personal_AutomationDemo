# Author:Yi Sun(Tim) 2023-08-29

"""Test Admin Page"""
from datetime import datetime
from pages.admin_page import AdminPage
from tests.ui.base_test import BaseUITest


class AdminUITest(BaseUITest):
    RESET_EACH_TEST = False          # open the home page once per class

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.driver.get(cls.base_url)
        cls.admin_page = AdminPage(cls.driver).wait_until_loaded()

    def test_adminportal_ui_001(self):
        '''Verify the url of Admin login Page'''
        self.assertEqual(self.base_url, self.admin_page.current_url)

    def test_adminportal_ui_002(self):
        '''Verify the default Sections in Admin login Page'''
        self.assertEqual(['Test Sample 1','Test Sample 2','Test Sample 3'], self.admin_page.get_top_menu_texts())

    def test_adminportal_ui_003(self):
        '''Verify the Find Quote in Admin Login page'''
        self.assertTrue(self.admin_page.is_search_box_displayed('quote'))

    def test_adminportal_ui_004(self):
        '''Verify the Find Address in Admin Login page'''
        self.assertTrue(self.admin_page.is_search_box_displayed('address'))

    def test_adminportal_ui_005(self):
        '''Verify the Find Client in Admin Login page'''
        self.assertTrue(self.admin_page.is_search_box_displayed('client'))

    def test_adminportal_ui_006(self):
        '''Verify the Quotes Menu'''
        self.assertEqual(['Test Sample 1','Test Sample 2','Test Sample 3'],self.admin_page.get_quotes_menu_items())

    def test_adminportal_ui_007(self):
        '''Verify the Services Menu'''
        self.assertEqual(['Test Sample 1','Test Sample 2','Test Sample 3'],self.admin_page.get_services_menu_items())

    def test_adminportal_ui_008(self):
        '''Verify the Lists Menu'''
        self.assertEqual(['Test Sample 1','Test Sample 2','Test Sample 3'], self.admin_page.get_list_menu_items())

    def test_adminportal_ui_009(self):
        '''Verify the Account Menu'''
        self.assertEqual(['Test Sample 1','Test Sample 2','Test Sample 3'], self.admin_page.get_account_menu_items())

    def test_adminportal_ui_010(self):
        '''Verify the Copyright and Terms'''
        self.assertEqual([f'© {datetime.now().year} - Test Sample', 'Terms and Policies'],
                         self.admin_page.get_footer_texts())


if __name__ == '__main__':
    unittest.main(verbosity=2)
