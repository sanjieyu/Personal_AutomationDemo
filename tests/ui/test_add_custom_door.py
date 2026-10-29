# Author:Yi Sun(Tim) 2023-9-16

'''Test Add a Custom Door Functian'''

from pages.add_custom_door import Add_Custom_Door
from pages.admin_page import AdminPage
from tests.ui.base_test import BaseUITest

class Add_CustomDoor_Fun_Test(BaseUITest):
    RESET_EACH_TEST = False  # navigate once per class, like the old setUpClass style

    @classmethod
    def setUpClass(cls):
        super().setUpClass()                                   # reuse the shared, logged-in browser
        cls.driver.get(cls.base_url)
        AdminPage(cls.driver).wait_until_loaded()
        cls.add_custom_door_page = Add_Custom_Door(cls.driver).add_quopte()
        cls.add_custom_door_page.open_custom_door()

    def test_add_customdoor_fun_001(self):
        '''Verify the input validation when add a new door'''
        self.driver.implicitly_wait(2)
        self.assertIn(('Test Sample 1','Test Sample 2','Test Sample 3'),self.add_custom_door_page.validation_input())

    def test_add_customdoor_fun_002(self):
        '''Verify the add door function'''
        self.add_custom_door_page.add_custom_detail()
        self.assertEqual(('Test Sample, name, colour (10 x 60)'), self.add_custom_door_page.new_added_custom_door())
    def test_add_customdoor_fun_003(self):
        '''Verify the duplicate button for the new added door'''
        self.driver.implicitly_wait(2)
        self.assertEqual(True, self.duplicate_btn)

    def test_add_customdoor_fun_004(self):
            '''Verify the delete button for the new added door'''
            self.driver.implicitly_wait(2)
            self.assertEqual(True, self.delete_btn)

if __name__ == '__main__':
    unittest.main(verbosity=2)