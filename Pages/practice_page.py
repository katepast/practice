import logging

from selenium.webdriver.common.by import By
from Pages.base_page import BasePage
from controls.Input import Input
from controls.multiple_selector import MultipleSelector
from controls.radio_button import RadioButton
from controls.selector import Selector


class PracticePage(BasePage):

    BMW_RADIO_BTN = (By.XPATH, ".//input[@id='bmwradio']")

    def __init__(self, driver):
        super().__init__(driver)
        self.bmw_radio_btn = RadioButton(driver=driver, label='bmw')
        self.benz_radio_btn = RadioButton(driver=driver, label='benz')
        self.honda_radio_btn = RadioButton(driver=driver, label='honda')
        self.enter_your_name_input = Input(driver=driver, placeholder="Enter Your Name")
        self.confirm_btn = Input(driver=driver, locator=(By.XPATH, ".//input[@id='confirmbtn']"))
        self.alert_btn = Input(driver=driver, locator=(By.XPATH, ".//input[@id='alertbtn']"))
        self.option_selector = Selector(driver=driver, option="Select Class Example")
        self.multiple_selector = MultipleSelector(driver=driver, legend="Multiple Select Example")

        # web table
        self.table = ".//table[@id='product']"
        self.tbody = ".//tbody"
        self.table_rows = ".//table[@id='product']//tr"

    def get_title_columns_from_table(self):
        table_xpath = self.driver.find_element_by_xpath(self.tbody)
        return [row.text for row in table_xpath.find_elements_by_tag_name("th")]

    def get_amount_of_rows_in_table(self):
        res = str(len(self.driver.find_elements_by_xpath(self.table_rows)))
        logging.debug("Founded amount of rows in the table", res)
        return res

    def get_values_for_author_column(self):
        logging.debug("Founded values for specified column 'Author' in the table")
        author_rows = self.driver.find_elements_by_xpath(".//td[@class='author-name']")
        return [row.text for row in author_rows]

    def get_values_for_course_column(self):
        logging.debug("Founded values for specified column 'Course' in the table")
        author_rows = self.driver.find_elements_by_xpath(".//td[@class='course-name']")
        return [row.text for row in author_rows]

    def get_values_for_price_column(self):
        logging.debug("Founded values for specified column 'Price' in the table")
        author_rows = self.driver.find_elements_by_xpath(".//td[@class='price']")
        return [row.text for row in author_rows]

    def check_bmw_radio_btn(self):
        """ Method to check radiobutton 'BMW' """
        logging.debug("Method to check radiobutton 'BMW'")
        self.bmw_radio_btn.select_radio_btn()

    def is_bmw_radio_btn_checked(self):
        logging.debug("Get current status of 'BMW' radio button")
        return self.bmw_radio_btn.get_radio_btn_status()

    def is_benz_radio_btn_checked(self):
        logging.debug("Get current status of 'Benz' radio button")
        return self.benz_radio_btn.get_radio_btn_status()

    def is_bmw_radio_btn_unchecked(self):
        logging.debug("Get current status of 'BMW' radio button")
        return self.bmw_radio_btn.is_rb_unselected()

    def check_all_radiobuttons(self):
        for rb in [self.bmw_radio_btn, self.benz_radio_btn, self.honda_radio_btn]:
            rb.select_radio_btn()

    def is_honda_radio_btn_checked(self):
        logging.debug("Get current status of 'Honda' radio button")
        return self.honda_radio_btn.get_radio_btn_status()

    def set_name(self, value):
        self.enter_your_name_input.send_keys(value)

    def get_name(self):
        return self.enter_your_name_input.get_value()

    def click_on_confirm_btn(self):
        self.confirm_btn.is_element_present()
        self.confirm_btn.click()

    def click_on_alert_btn(self):
        self.alert_btn.is_element_present()
        self.alert_btn.click()

    def is_alert_displayed(self):
        return self.driver.wait_till_alert_is_present(driver=self.driver)

    def confirm_alert(self):
        alert = self.driver.switch_to_alert()
        alert.accept()

    def is_alert_not_displayed(self):
        return self.driver.wait_till_alert_is_present()

    def get_alert_text(self):
        logging.debug("Get alert text")
        return self.driver.get_alert_text()

    def select_option_from_selector(self, text):
        logging.debug("Select option by visible text")
        self.option_selector.select_by_text(text)

    def get_current_value(self):
        logging.debug("Get current value")
        return self.option_selector.get_selected_value()

    def get_all_available_values(self):
        logging.debug("Get all available values")
        return self.option_selector.get_all_options()

    def is_multiple_sel_displayed(self):
        return self.multiple_selector.is_element_displayed()

    def select_multiple_element_from_multi_sel(self, text):
        logging.debug("Select multiple element from multi selector")
        self.multiple_selector.select_element(text)

    def get_selected_elements_from_multi_sel(self):
        logging.debug("Get value from multi selector")
        return self.multiple_selector.get_selected_elements()
