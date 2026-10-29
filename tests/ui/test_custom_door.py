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
        '''Verify the main elements in the page, should including correct title, Add button and Close button '''
        self.assertEqual(('Custom Door Details'),self.custom_door_page.get_modal_title())

    def test_customdoor_ui_002(self):
        '''Verify each element for install details, should including "Install Type","Design","Colour Category","Door Colour","Frame Colour",
        "Timber Profile","Insert Material","Insert Location","Insert Type","Insert Other" and "Custom Colour" '''
        self.assertEqual(['Install Type','Design','Colour Category','Door Colour','Frame Colour','Timber Profile',
                          'Insert Material','Insert Location','Insert Type','Insert Colour','Insert Other',
                          'Custom Colour'],self.custom_door_page.check_install_details())
    #
    def test_customdoor_ui_003(self):
        '''Verify the Install Type dropdown list, should including "Commercial Cat 1","Commercial Cat 2","Commercial STD","Panel Replacement" and "Residential" '''
        self.assertEqual(['Please Select','Commercial Cat 1','Commercial Cat 2','Commercial STD',
                          'Full Panel Replacement','Residential'],self.custom_door_page.check_install_type())
    #
    def test_customdoor_ui_004(self):
            '''Verify the Design dropdown list, should including "Ali Batten","Ali Louvre Panel","Aliwood","Alumicomp","Bar panel","Barn Panel",
            "Carriage Panel","Cedar Panel 135","Cedar Panel 86","Classic Panel","Frame Only STD","Frame Only Welded","Glasslite","Grille Panel","Herringbone Panel",
            "Louvre Panel","Perfalite","Raised Panel","Recessed Panel","Tranquilo Panel","Twinlight" and "Verti Panel" '''
            self.assertEqual(['Please Select','Ali Batten','Ali Louvre Panel','Aliwood','Alumalite','Alumicomp','Bar panel',
                           'Barn Panel','Carriage Panel','Cedar Batten','Cedar Panel 135','Cedar Panel 86',
                           'Classic Panel','Frame Only STD','Frame Only Welded','Glasslite','Grille Panel',
                           'Herringbone Panel','Louvre Panel','Perfalite','Raised Panel','Recessed Panel',
                           'Tranquilo Panel','Twinlight','Verti Panel'],self.custom_door_page.check_design())
    #
    def test_customdoor_ui_005(self):
            '''Verify the Colour Category dropdown list, should including "Custom","OilColour","Painted","PowderCoatStandard","PowderCoatUpgrade","Primed","Raw" and "SealedColour" '''
            self.assertEqual(['Please Select','Custom','OilColour','Painted','PowderCoatStandard','PowderCoatUpgrade','Primed',
                           'Raw','SealedColour'],self.custom_door_page.check_colour_category())

    def test_customdoor_ui_006(self):
            '''Verify the Door Colour dropdown list should be diabled if select "Custom" in Colour Category '''
            self.custom_door_page.select_colour_category("Custom")
            self.assertFalse(self.custom_door_page.is_door_colour_enabled())

    def test_customdoor_ui_007(self):
        '''Verify the Door Colour dropdown if select "OilColour" in Colour Category '''
        self.assertEqual(['Please Select','Black Ash','Clear','Custom','Sela Brown','TBA'],
                         self.custom_door_page.check_door_colour_options("OilColour"))
    #
    def test_customdoor_ui_008(self):
            '''Verify the Door Colour dropdown if select "Painted" in Colour Category '''
            self.assertEqual(['Please Select','Custom Colour'], self.custom_door_page.check_door_colour_options("Painted"))

    def test_customdoor_ui_009(self):
            '''Verify the Door Colour dropdown if select "SealedColour" in Colour Category '''
            self.assertEqual(['Please Select',
                              'Anotec® Dark Grey Matt',
                              'Anotec® Mid Bronze Matt',
                              'Anotec® Silver Grey Matt',
                              'APO Grey Satin',
                              'Basalt® Matt',
                              'Basalt® Satin',
                              'Berry Grey Gloss',
                              'Berry Grey Satin',
                              'Black (Night Sky®) Matt',
                              'Black (Night Sky®) Satin',
                              'Black Gloss',
                              'Blue Ridge® Satin',
                              'Bluegum® Matt',
                              'Bright White Gloss',
                              'Charcoal Gloss',
                              'Charcoal Matt',
                              'Charcoal Satin',
                              'Classic Cream™ Matt',
                              'Classic Cream™ Satin',
                              'Classic Pearl White Gloss',
                              'Cottage Green® Satin',
                              'Cove® Satin',
                              'Deep Brunswick Green Gloss',
                              'Deep Ocean® Matt',
                              'Deep Ocean® Satin',
                              'Dover White™ Matt',
                              'Dune® Matt',
                              'Dune® Satin',
                              'Evening Haze® Satin',
                              'Grey Nurse Gloss',
                              'Gully® Satin',
                              'Hammersley Brown Satin',
                              'Ironstone® Matt',
                              'Ironstone® Satin',
                              'Jasper® Matt',
                              'Jasper® Satin',
                              'Lexicon® Quarter Matt',
                              'Mangrove Satin',
                              'Manor Red® Satin',
                              'Monument® Matt',
                              'Monument® Satin',
                              'Natural White™ Matt',
                              'Navy Blue Gloss',
                              'Notre Dame Gloss',
                              'Old Pewter Satin',
                              'Oyster Matt Matt',
                              'Pale Eucalypt® Matt',
                              'Pale Eucalypt®  Satin',
                              'Paperbark® Matt',
                              'Paperbark® Satin',
                              'Pearl White Gloss',
                              'Pink Sand Matt',
                              'Primrose Gloss',
                              'Rivergum Beige Gloss',
                              'Riversand® Matt',
                              'Shale Grey™ Matt',
                              'Shale Grey™ Satin',
                              'Shoji White Satin',
                              'Southerly® Matt',
                              'Stone Beige Matt',
                              'Stone Grey Satin',
                              'Surfmist® Matt',
                              'Surfmist® Satin',
                              'Terrain®  Satin',
                              'Territory Red  Matt',
                              'Transformer Grey Gloss',
                              'Wallaby® Satin',
                              'Wallaby®  Matt',
                              'Wedgewood Satin',
                              'Whisper White Matt',
                              'White Matt',
                              'White Birch Gloss',
                              'White Satin',
                              'Wilderness® Satin',
                              'Windspray® Matt',
                              'Windspray® Satin',
                              'Wollemi® Matt',
                              'Woodland Grey® Matt',
                              'Woodland Grey® Satin'],
                             self.custom_door_page.check_door_colour_options("PowderCoatStandard"))

    def test_customdoor_ui_010(self):
            '''Verify the Door Colour dropdown if select "Raw" in Colour Category '''
            self.assertEqual(['Please Select','TBA'], self.custom_door_page.check_door_colour_options("Raw"))

    def test_customdoor_ui_011(self):
            '''Verify the Door Colour dropdown if select "SealedColour" in Colour Category '''
            self.assertEqual(['Please Select','Clear','Custom','Dark oak','Ebony','Hemlock','Light oak',
                              'Rosewood','TBA','Walnut'], self.custom_door_page.check_door_colour_options("SealedColour"))

    def test_customdoor_ui_012(self):
            '''Verify the Frame Colour dropdown list '''
            self.assertEqual(['Please Select','Clear','Custom','Dark oak','Ebony','Hemlock','Light oak','Rosewood',
 'TBA','Walnut','Mill Finish'], self.custom_door_page.check_frame_colour())

    def test_customdoor_ui_013(self):
            '''Verify the Timber Profile dropdown list,should includes "135mm Shiplap","135mm V-Join","86mm Shiplap" and "86mm V-Join" '''
            self.assertEqual(['Please Select','135mm Shiplap','135mm V-Join','86mm Shiplap','86mm V-Join'],
                             self.custom_door_page.check_timber_profile())

    def test_customdoor_ui_014(self):
            '''Verify the Insert Material dropdown list,should includes "ACPS Upgrade - Cat 1","ACPS Upgrade - Cat 2","Acrylic","Aluminium","Exterier Ply","Glass","Other",
             "Polycarbonate","Standard ACPS","Supplied By Client" and "TBA" '''
            self.assertEqual(['Please Select','ACPS Upgrade - Cat 1','ACPS Upgrade - Cat 2','Acrylic','Aluminium',
                           'Exterier Ply','Glass','Other','Polycarbonate','Standard ACPS','Supplied By Client','TBA'],
                          self.custom_door_page.check_insert_material())

    def test_customdoor_ui_015(self):
            '''Verify the Insert Location dropdown list,should includes "Face Fixed","Inserted into Frame" and "TBA" '''
            self.assertEqual(['Please Select','Face Fixed','Inserted into Frame','TBA'],
                             self.custom_door_page.check_insert_location())

    def test_customdoor_ui_016(self):
            '''Verify Insert Type dropdown list, the default value should be empty '''
            self.assertEqual(['Please Select'], self.custom_door_page.check_insert_type_options("Please Select"))

    def test_customdoor_ui_017(self):
            '''Verify the Insert Type dropdown if select "ACPS Cat1" in Insert Material category,should includes "Alutile",
            "Other","Ultrabond" and "Vitrabond"'''
            self.assertEqual(['Please Select','Alutile','Other','Ultrabond','Vitrabond'],
                             self.custom_door_page.check_insert_type_options("ACPS Upgrade - Cat 1"))

    def test_customdoor_ui_018(self):
            '''Verify the Insert Type dropdown if select "ACPS Cat2" in Insert Material category,should includes "Alpolic",
            "Alucabond","Other" and "Symonite"'''
            self.assertEqual(['Please Select','Alpolic','Alucabond','Other','Symonite'],
                             self.custom_door_page.check_insert_type_options("ACPS Upgrade - Cat 2"))

    def test_customdoor_ui_019(self):
            '''Verify the Insert Type dropdown if select "Acrylic" in Insert Material category,should includes "3mm Acrylic" and "6mm Acrylic"'''
            self.assertEqual(['Please Select','3mm Acrylic','4.5mm Acrylic','6mm Acrylic'],
                             self.custom_door_page.check_insert_type_options("Acrylic"))

    def test_customdoor_ui_020(self):
            '''Verify the Insert Type dropdown if select "Aluminium" in Insert Material category,should includes
            "CLOVERLEAF - 36%","Other","P1012SQ - 10mm Square-70%","P1925 - 19mm Round-51%","P1931SR - 19x3mm slots-41%",
             "P2031 - 2MM Round-41%","P2332HEX - 23mm Hexagon-44%","P2563SR - 25x6.3mm slots-43%","P3247 - 3.2mm Round-41%",
             "P4763 - 4.7mm Round-51%","P4769 - 4.7mm Square-47%","P5512SD - 5.5mm Square-19%",
              "P7995 - 7.9mm Round-62%" and "P9511HEX - 11.9mm Hexagon-64%"'''
            self.assertEqual(['Please Select','CLOVERLEAF - 36%','Other','P1012SQ - 10mm Square-70%',
                              'P1925 - 19mm Round-51%','P1931SR - 19x3mm slots-41%','P2031 - 2MM Round-41%',
                              'P2332HEX - 23mm Hexagon-44%','P2563SR - 25x6.3mm slots-43%','P3247 - 3.2mm Round-41%',
                              'P4763 - 4.7mm Round-51%','P4769 - 4.7mm Square-47%','P5512SD - 5.5mm Square-19%',
                              'P7995 - 7.9mm Round-62%','P9511HEX - 11.9mm Hexagon-64%'],
                             self.custom_door_page.check_insert_type_options("Aluminium"))
    def test_customdoor_ui_021(self):
            '''Verify the Insert Type dropdown if select "Exterier Ply" in Insert Material category,'''
            self.assertEqual(['Please Select','12mm','3mm','4mm','6mm','9mm','TBA'],
                             self.custom_door_page.check_insert_type_options("Exterier Ply"))

    def test_customdoor_ui_022(self):
            '''Verify the Insert Type dropdown if select "Glass" in Insert Material category,'''
            self.assertEqual(['Please Select','Other','Supergray','TBA'],self.custom_door_page.check_insert_type_options("Glass"))

    def test_customdoor_ui_023(self):
            '''Verify the Insert Type dropdown if select "Polycarbonate" in Insert Material category,'''
            self.assertEqual(['Please Select','10mm Twincore'],self.custom_door_page.check_insert_type_options("Polycarbonate"))

    def test_customdoor_ui_024(self):
            '''Verify the Insert Type dropdown if select "Standard ACPS" in Insert Material category,'''
            self.assertEqual(['Please Select','Standard ACPS'],self.custom_door_page.check_insert_type_options("Standard ACPS"))

    def test_customdoor_ui_025(self):
            '''Verify the Insert Type dropdown if select "TBA" in Insert Material category,'''
            self.assertEqual(['Please Select','TBA'],self.custom_door_page.check_insert_type_options("TBA"))

if __name__ == '__main__':
    unittest.main(verbosity=2)