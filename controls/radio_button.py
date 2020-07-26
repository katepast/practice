from distutils import log
from selenium.webdriver.common.by import By

from controls.base_control import BaseControl


class RadioButton(BaseControl):
    """
        Represents classic HTML radio button.
        :param label: label for radio button
        :param driver: instance of WebDriver
        """

    RADIO_BUTTON_xpath = ".//div[@id='radio-btn-example']//input[@type='radio' and @value='{}']"

    def __init__(self, driver, label, locator=None):
        super().__init__(driver)
        if locator:
            self._locator = locator
        else:
            self._locator = (By.XPATH, self.RADIO_BUTTON_xpath.format(label))

    def select_radio_btn(self):
        log.debug("Method to select radio button")
        radio_btn = self._get_web_element()
        radio_btn.click()

    def get_radio_btn_status(self):
        log.debug("Method to get current state of radio button")
        try:
            radio_btn = self._get_web_element()
            return radio_btn.is_selected()
        except:
            print("Radio button is not selected")
            return False

    def is_rb_unselected(self):
        radiobuton = self._get_web_element()
        return not radiobuton.is_selected()
