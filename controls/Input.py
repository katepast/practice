from selenium.webdriver.common.by import By
from controls.base_control import BaseControl


class Input(BaseControl):
    """ Control to describe input methods"""

    INPUT_XPATH = ".//input[@type='text' and @placeholder='{}']"

    def __init__(self, driver, placeholder=None, locator=None):
        super().__init__(driver)
        if locator:
            self._locator = locator
        else:
            self._locator = (By.XPATH, self.INPUT_XPATH.format(placeholder))

    def send_keys(self, value):
        el = self._get_web_element()
        return el.send_keys(value)
