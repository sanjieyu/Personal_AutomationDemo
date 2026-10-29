# Author:Yi Sun(Tim) 2023-9-16

'''Test Add Custom Door Page'''

from pages.custom_door_page import Custom_Door
from pages.admin_page import AdminPage
from tests.ui.base_test import BaseUITest

class CustomDoorUITest(BaseUITest):
    RESET_EACH_TEST = False  # navigate once per class, like the old setUpClass style

    @classmethod
    def setUpClass(cls):
        super().setUpClass()                                   # reuse the shared, logged-in browser
        cls.driver.get(cls.base_url)
        AdminPage(cls.driver).wait_until_loaded()
        cls.custom_door_page = Custom_Door(cls.driver).add_quote()
        cls.custom_door_page.open_custom_door()

    def test_customdoor_ui_001(self):
        '''Verify the main elements in the page'''
        self.assertEqual(('Test Sample Details'),self.custom_door_page.get_modal_title())

    def test_customdoor_ui_002(self):
        '''Verify each element for install details'''
        self.assertEqual(['Test Sample 1','Test Sample 2','Test Sample 3','Test Sample 4',
                                                          'Test Sample 5'],self.custom_door_page.check_install_details())
    #
    def test_customdoor_ui_003(self):
        '''Verify the Install Type dropdown list'''
        self.assertEqual(['Test Sample 1','Test Sample 2','Test Sample 3','Test Sample 4',
                                                          'Test Sample 5'],self.custom_door_page.check_install_type())
    #
    def test_customdoor_ui_004(self):
            '''Verify the Design dropdown list'''
            self.assertEqual(['Test Sample 1','Test Sample 2','Test Sample 3','Test Sample 4',
                                                          'Test Sample 5'],self.custom_door_page.check_design())
    #
    def test_customdoor_ui_005(self):
            '''Verify the Colour Category dropdown list'''
            self.assertEqual(['Test Sample 1','Test Sample 2','Test Sample 3','Test Sample 4',
                                                          'Test Sample 5'],self.custom_door_page.check_colour_category())

    def test_customdoor_ui_006(self):
            '''Verify the Door Colour dropdown list should be diabled if select "Custom" in Colour Category '''
            self.custom_door_page.select_colour_category("Custom")
            self.assertFalse(self.custom_door_page.is_door_colour_enabled())

    def test_customdoor_ui_007(self):
        '''Verify the Door Colour dropdown if select "Colour Sample 2" in Colour Category '''
        self.assertEqual(['Test Sample 1','Test Sample 2','Test Sample 3'],
                         self.custom_door_page.check_door_colour_options("Colour Sample 2"))
    #
    def test_customdoor_ui_008(self):
            '''Verify the Door Colour dropdown if select "Colour Sample 1" in Colour Category '''
            self.assertEqual(['Please Select','Test Sample'], self.custom_door_page.check_door_colour_options("Colour Sample 1"))

    def test_customdoor_ui_009(self):
            '''Verify the Door Colour dropdown if select "Test Sample" in Colour Category '''
            self.assertEqual(['Test Sample 1','Test Sample 2','Test Sample 3'],
                             self.custom_door_page.check_door_colour_options("Test Sample"))

    def test_customdoor_ui_010(self):
            '''Verify the Door Colour dropdown if select "Test Sample" in Colour Category '''
            self.assertEqual(['Please Select','Test Sample'], self.custom_door_page.check_door_colour_options("Test Sample"))

    def test_customdoor_ui_011(self):
            '''Verify the Door Colour dropdown if select "Test Sample" in Colour Category '''
            self.assertEqual(['Test Sample 1','Test Sample 2','Test Sample 3'],
                             self.custom_door_page.check_door_colour_options("Test Sample"))

    def test_customdoor_ui_012(self):
            '''Verify the Frame Colour dropdown list '''
            self.assertEqual(['Test Sample 1','Test Sample 2','Test Sample 3'], self.custom_door_page.check_frame_colour())

    def test_customdoor_ui_013(self):
            '''Verify the Timber Profile dropdown list'''
            self.assertEqual(['Test Sample 1','Test Sample 2','Test Sample 3'],self.custom_door_page.check_timber_profile())

    def test_customdoor_ui_014(self):
            '''Verify the Insert Material dropdown list'''
            self.assertEqual(['Test Sample 1','Test Sample 2','Test Sample 3'],self.custom_door_page.check_insert_material())

    def test_customdoor_ui_015(self):
            '''Verify the Insert Location dropdown list'''
            self.assertEqual(['Test Sample 1','Test Sample 2','Test Sample 3'],self.custom_door_page.check_insert_location())

    def test_customdoor_ui_016(self):
            '''Verify Insert Type dropdown list, the default value should be empty '''
            self.assertEqual(['Please Select'], self.custom_door_page.check_insert_type_options("Please Select"))

    def test_customdoor_ui_017(self):
            '''Verify the Insert Type dropdown if select "Test Sample 1" in Insert Material category'''
            self.assertEqual(['Test Sample 1','Test Sample 2','Test Sample 3'],
                             self.custom_door_page.check_insert_type_options("Test Sample 1"))

    def test_customdoor_ui_018(self):
            '''Verify the Insert Type dropdown if select "Test Sample 2" in Insert Material category'''
            self.assertEqual(['Test Sample 1','Test Sample 2','Test Sample 3'],
                             self.custom_door_page.check_insert_type_options("Test Sample 2"))

    def test_customdoor_ui_019(self):
            '''Verify the Insert Type dropdown if select "Test Sample 3" in Insert Material category'''
            self.assertEqual(['Test Sample 1','Test Sample 2','Test Sample 3'],
                             self.custom_door_page.check_insert_type_options("Test Sample 3"))

    def test_customdoor_ui_020(self):
            '''Verify the Insert Type dropdown if select "Test Sample 4" in Insert Material category'''
            self.assertEqual(['Test Sample 1','Test Sample 2','Test Sample 3'],
                             self.custom_door_page.check_insert_type_options("Test Sample 4"))
    def test_customdoor_ui_021(self):
            '''Verify the Insert Type dropdown if select "Test Sample 5" in Insert Material category,'''
            self.assertEqual(['Test Sample 1','Test Sample 2','Test Sample 3'],
                             self.custom_door_page.check_insert_type_options("Test Sample 5"))

    def test_customdoor_ui_022(self):
            '''Verify the Insert Type dropdown if select "Test Sample" in Insert Material category,'''
            self.assertEqual(['Test Sample 1','Test Sample 2','Test Sample 3'],
                             self.custom_door_page.check_insert_type_options("Test Sample"))

    def test_customdoor_ui_023(self):
            '''Verify the Insert Type dropdown if select "Test Sample" in Insert Material category,'''
            self.assertEqual(['Test Sample 1','Test Sample 2'],self.custom_door_page.check_insert_type_options("Test Sample"))

    def test_customdoor_ui_024(self):
            '''Verify the Insert Type dropdown if select "Test Sample" in Insert Material category,'''
            self.assertEqual(['Test Sample 1','Test Sample 2'],self.custom_door_page.check_insert_type_options("Test Sample"))

    def test_customdoor_ui_025(self):
            '''Verify the Insert Type dropdown if select "Test Sample" in Insert Material category,'''
            self.assertEqual(['Test Sample 1','Test Sample 2'],self.custom_door_page.check_insert_type_options("Test Sample"))

if __name__ == '__main__':
    unittest.main(verbosity=2)