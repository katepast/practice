from distutils import log
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from controls.base_control import BaseControl


class MultipleSelector(BaseControl):

    MultipleSelector_XPATH = ".//legend[normalize-space(.)='{}']/following::select[@id='multiple-select-example']"

    def __init__(self, driver, legend=None, locator=None):
        super().__init__(driver)
        if legend:
            self._locator = (By.XPATH, self.MultipleSelector_XPATH.format(legend))
        elif locator:
            self._locator = locator
        else:
            self._locator = (By.TAG_NAME, "select")
        self.options = (By.TAG_NAME, "option")

    def select_element(self, text):
        """Select element by visible text"""
        log.debug("Select element by visible text")
        element = self._get_web_element()
        return Select(element).select_by_visible_text(text=text)

    def get_selected_elements(self):
        """
        Get all selected elements from selector
        :return: text from selected elements
        """
        log.debug("Get all selected elements from selector")
        element = self._get_web_element()
        results = element.find_elements(*self.options)
        return [el.text for el in results]
