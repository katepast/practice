from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait


class BaseControl:
    """
    Represents base class UI controls
    :param driver: instance of WebDriver
    :param label: label for group control, used in locator
    :param locator: locator of element (optional)

    """
    def __init__(self, driver):
        self._driver = driver
        self.__locator = None

    @property
    def _locator(self):
        """Returns Control locator"""
        return self.__locator

    @_locator.setter
    def _locator(self, locator):
        """
        Set Control locator
        :param locator: tuple (By.<CSS/XPATH/etc>, 'locator')
        """
        if not isinstance(locator, tuple):
            raise ValueError("Locator must be a tuple (By.<CSS/XPATH/etc>, 'locator')")
        self.__locator = locator

    def _get_web_element(self):
        """
        Waits for a parent and gets WebElement of locator
        :return: WebElement of _locator
        """
        return self._driver.find_element(*self._locator)

    def is_element_present(self):
        """Return whether specified element elector is present on the page"""
        try:
            self._get_web_element()
            return True
        except:
            return False

    def is_element_displayed(self):
        """Returns whether specified element elector is visible on the page"""
        try:
            element = self._get_web_element()
            return element.is_displayed()
        except:
            return False

    def get_attr(self, attr_name):
        """
        Get attribute value of WebElement
        :param attr_name: name of attribute
        :return: value of attribute
        """
        return self._get_web_element().get_attribute(attr_name)

    def get_value(self):
        """
        Get value of WebElement
        :return: value of attribute
        """
        return self._get_web_element().get_attribute("value")

    def get_text(self):
        """
        Gets 'text' property of Selenium's WebElement
        :return:
        """
        return self._get_web_element().text

    def click(self):
        """
        Waits for element becomes clickable and performs click
        """
        element = self._get_web_element()
        actions = ActionChains(self._driver)
        actions.move_to_element(element)
        return element.click()

    def double_click(self):
        """
        Waits for element becomes clickable and performs doubleclick
        """
        element = self._get_web_element()
        actions = ActionChains(self._driver)
        actions.move_to_element(element)
        self._driver.double_click(element)

    def clear(self):
        """Clear Input field"""
        self._get_web_element().clear()

    def send_keys(self, new_value, clear=True):
        el = self._get_web_element().click()
        if clear:
            el.clear()
            el.send_keys(new_value)
        else:
            self._get_web_element().send_keys(new_value)

    def scroll_to_element(self):
        """
        Method to scroll to element
        """
        element = self._get_web_element()
        self._driver.execute_script("arguments[0].scrollIntoView(true);", element)
