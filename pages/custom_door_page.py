# Author:Yi Sun(Tim) 2023-11-02

'''Add Custom Door Details Page'''

from selenium.webdriver.common.by import By
from pages.add_quote_page import Add_Quote
from selenium.common.exceptions import TimeoutException
from contextlib import contextmanager

class Custom_Door(Add_Quote):
    """
        Note: For security and confidentiality, specific XPath/CSS selectors
        have been replaced with 'test_sample', and additional private locators
        have been omitted from this public sample.
    """
    add_door_section = (By.ID,"test_sample")
    add_custom_btn = (By.ID,"test_sample")
    add_btn_loc = (By.ID, "test_sample")
    close_customdoor_btn = (By.ID,"test_sample")
    door_main_page = (By.CSS_SELECTOR,"label[for='test_sample']")

    '''loc for each element for install details'''
    title_loc = (By.CSS_SELECTOR,"label[for='test_sample']")
    unit_no_loc = (By.CSS_SELECTOR,"label[for='test_sample']")
    unit_no_inputbox = (By.ID, "test_sample")
    packaging_type_loc = (By.CSS_SELECTOR, "test_sample")
    packaging_type_select = (By.ID, "test_sample")

    install_type_loc = (By.CSS_SELECTOR,"label[for='test_sample']")
    install_type_select = (By.ID,"test_sample")
    design_loc = (By.XPATH,"test_sample")
    design_select = (By.ID,"test_sample")
    colour_category_loc = (By.XPATH,"test_sample")
    colour_category_select = (By.ID,"test_sample")
    door_colour_loc = (By.XPATH,"test_sample")
    door_colour_select = (By.ID,"test_sample")
    frame_colour_loc = (By.XPATH,"test_sample")
    frame_colour_select = (By.ID,"test_sample")
    timber_profile_loc = (By.CSS_SELECTOR,"label[for='test_sample']")
    timber_profile_select = (By.ID,"test_sample")
    insert_material_loc = (By.CSS_SELECTOR,"label[for='test_sample']")
    insert_material_select = (By.ID,"test_sample")
    insert_location_loc = (By.CSS_SELECTOR,"label[for='test_sample']")
    insert_location_select= (By.ID,"test_sample")
    insert_type_loc = (By.XPATH,"//label[@for='CustomInsertType']")
    insert_type_select = (By.ID,"test_sample")
    insert_colour_loc = (By.XPATH,"//label[@for='CustomInsertColour']")
    insert_colour_select = (By.ID,"test_sample")
    insert_other_loc = (By.CSS_SELECTOR,"label[for='test_sample']")
    insert_other_inputbox = (By.ID,"test_sample")
    custom_colour_loc = (By.CSS_SELECTOR,"label[for='test_sample']")
    custom_colour_inputbox = (By.ID,"test_sample")

    '''loc for each element for SIZE details'''
    opensize_lh_loc = (By.XPATH,"test_sample")
    opensize_lh_select = (By.ID,"test_sample")
    opensize_rh_loc = (By.CSS_SELECTOR,"label[for='test_sample']")
    opensize_rh_select = (By.ID,"test_sample")
    opensize_width_loc = (By.CSS_SELECTOR,"label[for='test_sample']")
    opensize_width_select =(By.ID,"test_sample")
    sr_left_loc = (By.XPATH,"test_sample")
    sr_left_select =(By.ID,"test_sample")
    hr_loc = (By.XPATH,"test_sample")
    hr_select = (By.ID,"test_sample")
    sr_right_loc = (By.XPATH,"test_sample")
    sr_right_select =(By.ID,"test_sample")
    lhrk_loc = (By.XPATH,"test_sample")
    lhrk_select = (By.ID,"test_sample")
    sms_bracket_loc = (By.CSS_SELECTOR,"label[for='test_sample']")
    lsr_kit_loc = (By.CSS_SELECTOR,"label[for='test_sample']")
    timber_packers_loc = (By.CSS_SELECTOR,"label[for='test_sample']")
    timber_packers_select = (By.ID,"test_sample")
    taper_loc =(By.XPATH,"test_sample")
    taper_select = (By.ID,"test_sample")
    additional_fabrication_loc = (By.CSS_SELECTOR,"label[for='test_sample']")
    additional_fabrication_select = (By.ID,"test_sample")
    additional_fabrication_required_loc = (By.CSS_SELECTOR,"label[for='test_sample']")
    additional_fabrication_required_inputbox = (By.ID,"test_sample")
    shop_drawings_loc = (By.CSS_SELECTOR,"label[for='test_sample']")
    shop_drawings_select = (By.ID,"test_sample")
    lifting_equipment_loc = (By.CSS_SELECTOR,"label[for='test_sample']")
    lifting_equipment_btn = (By.CSS_SELECTOR,"label[for='test_sample']")

    '''loc for each element for Panels details'''
    panel_high_loc = (By.XPATH,"test_sample")
    panel_high_select_loc = (By.ID,"test_sample")
    panel_wide_loc = (By.XPATH, "test_sample")
    panel_wide_btn_loc = (By.CSS_SELECTOR,"test_sample")
    panel_wide_input_loc = (By.ID, "test_sample")

    '''loc for each element for checkboxes details'''
    induction_loop_loc = (By.XPATH,"//label[@for='test_sample']")
    reverse_install_loc = (By.XPATH,"//label[@for='test_sample']")
    fully_sloctted_loc = (By.XPATH,"//label[@for='test_sample']")
    emergency_key_loc = (By.XPATH,"//label[@for='test_sample']")
    reverse_colour_loc = (By.CSS_SELECTOR,"label[for='test_sample']")
    battery_backup_loc = (By.CSS_SELECTOR,"label[for='test_sample']")
    eco_wifi_loc = (By.CSS_SELECTOR,"label[for='test_sample']")

    '''loc for Opener details'''
    opener_loc = (By.XPATH,"//label[@for='test_sample']")
    opener_select = (By.ID,'test_sample')
    handsets_loc = (By.CSS_SELECTOR,"label[for='test_sample']")
    handsets_select = (By.ID,'test_sample')
    wall_btn_loc = (By.XPATH,"//label[@for='test_sample']")
    wall_btn_select = (By.ID,'test_sample')
    opener_detail_loc = (By.XPATH,"//label[@for='test_sample']")
    opener_detail_box = (By.ID,'test_sample')
    digital_keypad_loc = (By.XPATH,"//label[@for='test_sample']")
    digital_keypad_select = (By.ID,'test_sample')
    internal_pushbtn_loc = (By.CSS_SELECTOR,"label[for='test_sample']")
    internal_pushbtn_select = (By.ID,'test_sample')
    pe_beam_loc = (By.XPATH,"//label[@for='test_sample']")
    pe_beam_select = (By.ID,'test_sample')
    pe_beam_sets_loc = (By.XPATH,"//label[@for='test_sample']")
    pe_beam_sets_select = (By.ID,'test_sample')


    '''loc for other elements details '''
    weight_added_loc = (By.CSS_SELECTOR, "label[for='test_sample']")
    weight_added_select = (By.ID,'test_sample')
    seals_loc = (By.CSS_SELECTOR,"label[for='test_sample']")
    seals_select = (By.ID,'test_sample')
    hang_door_loc = (By.CSS_SELECTOR, "label[for='test_sample']")
    hang_door_select = (By.ID,'test_sample')
    lintel_type_loc = (By.CSS_SELECTOR, "label[for='CustomLintelType']")
    lintel_type_select = (By.ID,'test_sample')
    fixing_type_loc = (By.CSS_SELECTOR, "label[for='CustomFixingType']")
    fixing_type_select = (By.ID,'test_sample')

    ibeam_noggins_loc = (By.CSS_SELECTOR, "label[for='test_sample']")
    ibeam_noggins_select = (By.ID,'test_sample')
    remove_dispose_loc = (By.CSS_SELECTOR,"label[for='test_sample']")
    remove_dispose_select = (By.ID,'test_sample')
    job_status_loc = (By.XPATH,"//label[@for='test_sample']")
    job_status_select = (By.ID,'test_sample')
    expected_deliverydate_loc = (By.CSS_SELECTOR,"label[for='test_sample']")
    expected_deliverydate_box = (By.ID,'test_sample')


    '''loc for additional infomation details '''
    additional_info_loc = (By.XPATH,"//label[@for='test_sample']")
    additional_info_box = (By.ID,'test_sample')
    production_notes_loc = (By.XPATH,"test_sample")
    production_notes_box = (By.ID,'test_sample')

    '''loc for Extra and Site Pictures'''
    extras_loc = (By.CSS_SELECTOR,"label[for='test_sample']")
    site_picture_loc = (By.CSS_SELECTOR,"label[for='test_sample']")

    '''loc for each element in Extra'''
    lh_jamb_loc = (By.CSS_SELECTOR,"label[for='test_sample']")
    lh_jamb_select = (By.ID, 'test_sample')
    lh_size_loc = (By.XPATH,"test_sample")
    lh_size_width_btn = (By.CSS_SELECTOR,"test_sample")
    lh_size_depth_btn = (By.CSS_SELECTOR,"test_sample")
    lh_size_width_select = (By.XPATH, "test_sample")
    lh_size_depth_select = (By.ID, "test_sample")
    rh_jamb_loc = (By.XPATH,"test_sample")
    rh_jamb_select = (By.ID, "test_sample")
    rh_size_loc = (By.XPATH,"test_sample")
    rh_size_width_btn = (By.CSS_SELECTOR,"test_sample")
    rh_size_depth_btn = (By.CSS_SELECTOR,"test_sample")
    rh_size_width_select = (By.ID, "test_sample")
    rh_size_depth_select = (By.ID, "test_sample")

    lh_cover_type_loc = (By.CSS_SELECTOR,"label[for='test_sample']")
    lh_cover_select = (By.ID, "test_sample")
    lh_cover_width_size_loc = (By.CSS_SELECTOR,"label[for='test_sample']")
    lh_cover_width_btn = (By.CSS_SELECTOR,"test_sample")
    lh_cover_depth_btn = (By.CSS_SELECTOR,"test_sample")
    lh_cover_width_select = (By.ID, "test_sample")
    lh_cover_depth_select = (By.ID, "test_sample")
    lh_cover_colour_loc = (By.XPATH,"//label[@for='test_sample']")
    lh_cover_colour_select = (By.ID, "test_sample")
    rh_cover_type_loc = (By.CSS_SELECTOR,"label[for='test_sample']")
    rh_cover_select = (By.ID, "test_sample")
    rh_cover_width_size_loc = (By.CSS_SELECTOR,"label[for='test_sample']")
    rh_cover_width_btn = (By.CSS_SELECTOR,"test_sample")
    rh_cover_width_select = (By.ID, "test_sample")
    rh_cover_depth_select = (By.ID, "test_sample")
    rh_cover_colour_loc = (By.XPATH,"//label[@for='test_sample']")
    rh_cover_colour_select = (By.ID, "test_sample")

    SIZE_FIELDS = {  # field name used by get_size_field_default()
        "opening_lh": opensize_lh_select, "opening_rh": opensize_rh_select,
        "opening_width": opensize_width_select, "sr_left": sr_left_select,
        "hr": hr_select, "sr_right": sr_right_select,
    }

    # ================= private helpers =================
    def _label(self, locator) -> str:
        """Label text by PRESENCE (like the old .text): a label that is hidden gives '' instead of a 20s timeout."""
        return " ".join(self.find(locator).text.split())

    def _labels(self, *locators) -> list:
        return [self._label(loc) for loc in locators]

    def _menu_lines(self, locator) -> list:
        text = self.find_visible(locator).text
        return [line.strip() for line in text.splitlines() if line.strip()]

    def _read_combobox(self, toggle_locator, menu_locator) -> list:
        """Click the jQuery-UI combobox arrow and return the entries of the list that opens."""
        self.click(toggle_locator)
        return self._menu_lines(menu_locator)

    def _select_and_read_dependent(self, source_locator, text, dependent_locator) -> list:
        """Choose `text` in one dropdown, wait until the dropdown that depends on it has refreshed
        (replaces sleep), and return the dependent dropdown's options."""
        before = self.select_options(dependent_locator)
        self.select_by_text(source_locator, text)
        try:
            self._wait(5).until(lambda _driver: self.select_options(dependent_locator) != before)
        except TimeoutException:
            pass                          # the lists can legitimately be identical
        return self.select_options(dependent_locator)

    def _scroll_form_to_bottom(self) -> None:
        self.driver.execute_script("arguments[0].scrollIntoView(false);", self.find(self.door_main_page))

    @contextmanager
    def _extras_expanded(self):
        """Keep the 'Extras' section open inside the with-block and restore its previous state afterwards.
        (The old code clicked Extras by hand before and after every read and slept 2s in between.)"""
        opened_here = not self.is_visible(self.extras_panel_loc, timeout=1)
        if opened_here:
            self.click(self.extras_loc)
            self.find_visible(self.extras_panel_loc)
        self._scroll_form_to_bottom()
        try:
            yield
        finally:
            if opened_here:
                self.click(self.extras_loc)
                self.wait_until_invisible(self.extras_panel_loc)

    # ================= open / title =================
    def open_custom_door(self) -> "Custom_Door":
        """Add door > Custom, from the Add Quote page (replaces go_addcustomdoor)."""
        self.click(self.add_door_section)
        self.click(self.add_custom_btn)
        self.switch_to_latest_window()  # kept from the old code; a no-op while it is a modal
        return self.wait_until_modal_loaded()

    def wait_until_modal_loaded(self) -> "Custom_Door":
        # not named wait_until_loaded: that name belongs to Add_Quote (the Add Quote page itself)
        self.find_visible(self.title_loc, timeout=20)
        return self

    def get_modal_title(self) -> str:
        return self.text_of(self.title_loc)

    # ================= install details =================
    def check_install_details(self) -> list:
        return self._labels(
            self.install_type_loc, self.design_loc, self.colour_category_loc, self.door_colour_loc,
            self.frame_colour_loc, self.timber_profile_loc, self.insert_material_loc, self.insert_location_loc,
            self.insert_type_loc, self.insert_colour_loc, self.insert_other_loc, self.custom_colour_loc)

    def check_install_type(self) -> list:
        return self.select_options(self.install_type_select)

    def check_design(self) -> list:
        return self.select_options(self.design_select)

    def check_colour_category(self) -> list:
        return self.select_options(self.colour_category_select)

    def select_colour_category(self, category: str) -> None:
        self.select_by_text(self.colour_category_select, category)

    def is_door_colour_enabled(self) -> bool:
        return self.find(self.door_colour_select).is_enabled()

    def check_door_colour_options(self, category: str = None) -> list:
        """Door Colour options; with `category` first choose that Colour Category (ColorBond, OilColour,
        Painted, Raw, SealedColour, Flexigraphic, Flexographic, MetalFx, Painted Finish, Portabella, TimberFX ...)."""
        if category is None:
            return self.select_options(self.door_colour_select)
        return self._select_and_read_dependent(self.colour_category_select, category, self.door_colour_select)

    def check_frame_colour(self) -> list:
        return self.select_options(self.frame_colour_select)

    def check_timber_profile(self) -> list:
        return self.select_options_hidden(self.timber_profile_select)

    def check_insert_material(self) -> list:
        return self.select_options(self.insert_material_select)

    def check_insert_location(self) -> list:
        return self.select_options(self.insert_location_select)

    def check_insert_type_options(self, material: str = None) -> list:
        """Insert Type options; with `material` first choose that Insert Material (e.g. 'Acrylic',
        'Aluminium', 'ACPS Upgrade - Cat 1') and return the refreshed list."""
        if material is None:
            return self.select_options(self.insert_type_select)
        return self._select_and_read_dependent(self.insert_material_select, material, self.insert_type_select)

    def select_colour_category(self, category: str) -> None:
        self.select_by_text(self.colour_category_select, category)

    def get_door_colour_options(self, category: str = None) -> list:
        """Door Colour options; with `category` first choose that Colour Category (ColorBond, OilColour,
        Painted, Raw, SealedColour, Flexigraphic, Flexographic, MetalFx, Painted Finish, Portabella, TimberFX ...)."""
        if category is None:
            return self.select_options(self.door_colour_select)
        return self._select_and_read_dependent(self.colour_category_select, category, self.door_colour_select)

    def is_door_colour_enabled(self) -> bool:
        return self.find(self.door_colour_select).is_enabled()

    def check_customcolour_box(self) -> bool:
        return self.find(self.custom_colour_inputbox).is_enabled()


    # ================= size details =================
    def check_size_details(self) -> list:
        return self._labels(
            self.opensize_lh_loc, self.opensize_rh_loc, self.opensize_width_loc, self.sr_left_loc, self.hr_loc,
            self.sr_right_loc, self.lhrk_loc, self.sms_bracket_loc, self.lsr_kit_loc)


    def check_openinglh_default(self, field: str) -> str:
        """field: opening_lh / opening_rh / opening_width / sr_left / hr / sr_right"""
        return self.find(self.SIZE_FIELDS[field]).get_attribute("value")

    def check_lhrk_list(self) -> list:
        return self.select_options(self.lhrk_select)

    def check_timber_details(self) -> list:
        return self._labels(
            self.timber_packers_loc, self.taper_loc, self.additional_fabrication_loc,
            self.additional_fabrication_required_loc, self.shop_drawings_loc, self.lifting_equipment_loc)

    # ================= checkboxes / opener / other / notes =================
    def check_checkboxes_details(self) -> list:
        return self._labels(
            self.induction_loop_loc, self.reverse_install_loc, self.fully_sloctted_loc, self.emergency_key_loc,
            self.reverse_colour_loc, self.battery_backup_loc, self.eco_wifi_loc)

    def check_opener_details(self) -> list:
        # the old code also read self.keys_loc, which is not defined anywhere -> not included here
        return self._labels(
            self.opener_loc, self.handsets_loc, self.wall_btn_loc, self.opener_detail_loc,
            self.digital_keypad_loc, self.internal_pushbtn_loc, self.pe_beam_loc, self.pe_beam_sets_loc)

    def check_other_details(self) -> list:
        # the old code also read cut_date_loc / paint_date_loc / qc_date_loc / other_date_loc,
        # which are not defined anywhere -> not included here
        return self._labels(
            self.weight_added_loc, self.seals_loc, self.hang_door_loc, self.lintel_type_loc, self.fixing_type_loc,
            self.ibeam_noggins_loc, self.remove_dispose_loc, self.job_status_loc, self.expected_deliverydate_loc)

    def check_additional_details(self) -> list:
        return self._labels(self.additional_info_loc, self.production_notes_loc)

    def check_extra_picture(self) -> list:
        return self._labels(self.extras_loc, self.site_picture_loc)

    # ================= Extras section (expands / collapses itself) =================
    def check_jamb_extras(self) -> list:
        with self._extras_expanded():
            return self._labels(self.lh_jamb_loc, self.lh_size_loc, self.rh_jamb_loc, self.rh_size_loc)

    def lh_jamb_type(self) -> list:
        with self._extras_expanded():
            return self.select_options(self.lh_jamb_select)

    def lh_width_size(self) -> list:
        with self._extras_expanded():
            return self._read_combobox(self.lh_size_width_btn, self.lh_size_width_select)

    def lh_depth_size(self) -> list:
        with self._extras_expanded():
            return self._read_combobox(self.lh_size_depth_btn, self.lh_size_depth_select)

    def rh_jamb_type(self) -> list:
        with self._extras_expanded():
            return self.select_options(self.rh_jamb_select)

    def rh_width_size(self) -> list:
        with self._extras_expanded():
            return self._read_combobox(self.rh_size_width_btn, self.rh_size_width_select)

    def rh_depth_size(self) -> list:
        with self._extras_expanded():
            return self._read_combobox(self.rh_size_depth_btn, self.rh_size_depth_select)

    def get_cover_type_labels(self) -> list:
        with self._extras_expanded():
            return self._labels(
                self.lh_cover_type_loc, self.lh_cover_width_size_loc, self.lh_cover_colour_loc,
                self.rh_cover_type_loc, self.rh_cover_width_size_loc, self.rh_cover_colour_loc)

    def get_lh_cover_type_options(self) -> list:
        with self._extras_expanded():
            return self.select_options(self.lh_cover_select)

    def lh_cover_width_size(self) -> list:
        with self._extras_expanded():
            return self._read_combobox(self.lh_cover_width_btn, self.lh_cover_width_select)

    def lh_cover_depth_size(self) -> list:
        with self._extras_expanded():
            return self._read_combobox(self.lh_cover_depth_btn, self.lh_cover_depth_select)

    @property
    def lh_cover_type(self):
        '''check the list for LH Cover Type'''
        sleep(2)
        self.driver.find_element(*self.extras_loc).click()
        form_element = self.driver.find_element(*self.door_main_page)
        self.driver.execute_script("arguments[0].scrollIntoView(false);", form_element)
        self.driver.find_element(*self.lh_cover_select).click()
        lh_cover_list = self.driver.find_element(*self.lh_cover_select).text
        self.driver.find_element(*self.extras_loc).click()
        print(lh_cover_list)
        return  lh_cover_list

if __name__ == '__main__':
    # Debug run: right-click > Run in PyCharm, or:  python -m UIModule.custom_door_page
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
        Add_Quote(driver).add_quote()  # Add > Quote
        page = Custom_Door(driver).open_custom_door()  # Add door > Custom
        print(page.get_modal_title())
        print(page.check_install_details())
        print(page.check_install_type())
    finally:
        driver.quit()














































