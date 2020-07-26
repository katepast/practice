import logging

from selenium.webdriver.common.by import By
from Pages.base_page import BasePage
from controls.Input import Input
from controls.multiple_selector import MultipleSelector
from controls.radio_button import RadioButton
from controls.selector import Selector
from helpers.common_actions import CommonActions


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
        return CommonActions.wait_till_alert_is_present(driver=self.driver)

    def confirm_alert(self):
        alert = self.driver.switch_to_alert()
        alert.accept()

    def is_alert_not_displayed(self):
        return CommonActions.wait_till_alert_is_present(driver=self.driver)

    def get_alert_text(self):
        logging.debug("Get alert text")
        return CommonActions.get_alert_text(driver=self.driver, timeout=2)

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
        return  self.multiple_selector.is_element_displayed()

    def select_multiple_element_from_multi_sel(self, text):
        logging.debug("Select multiple element from multi selector")
        self.multiple_selector.select_element(text)

    def get_selected_elements_from_multi_sel(self):
        logging.debug("Get value from multi selector")
        return self.multiple_selector.get_selected_elements()
