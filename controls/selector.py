from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from controls.base_control import BaseControl


class Selector(BaseControl):

    SELECTOR_XPATH = ".//legend[text()='{}']/following::select[@id='carselect']"

    def __init__(self, driver, option=None):
        super().__init__(driver)
        if option:
            self._locator = (By.XPATH, self.SELECTOR_XPATH.format(option))
        else:
            self._locator = (By.TAG_NAME, "select")
        self.options = (By.TAG_NAME, "option")

    def select_by_text(self, text):
        """
        Select value by visible text
        :param text: option text to select
        """
        element = self._get_web_element()
        return Select(element).select_by_visible_text(text)

    def get_selected_value(self):
        element = self._get_web_element()
        return Select(element).first_selected_option.text

    def get_all_options(self):
        element = self._get_web_element()
        results = element.find_elements(*self.options)
        return [el.text for el in results]
