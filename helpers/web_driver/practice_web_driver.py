from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.abstract_event_listener import AbstractEventListener
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class WebDriverListener(AbstractEventListener):
    def before_find(self, by, value, driver):
        return WebDriverWait(driver, 4).until(EC.visibility_of_element_located((by, value)))


class WebDriver(EventFiringWebDriver):

    def wait_till_element_is_displayed(self, locator, timeout=10):
        wait = WebDriverWait(self._driver, timeout)
        try:
            wait.until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def wait_till_text_present(self, locator, text, timeout=10):
        wait = WebDriverWait(self._driver, timeout)
        try:
            return wait.until(EC.text_to_be_present_in_element(locator, text))
        except TimeoutException:
            return False

    def wait_till_element_checked(self, locator, timeout=10):
        wait = WebDriverWait(self._driver, timeout)
        try:
            return wait.until(EC.element_to_be_selected(locator))
        except TimeoutException:
            return False

    def wait_till_element_presents(self, locator, timeout=10):
        wait = WebDriverWait(self._driver, timeout)
        try:
            return wait.until(EC.presence_of_all_elements_located(locator))
        except TimeoutException:
            return False

    def wait_till_element_not_visible(self, locator, timeout=10):
        wait = WebDriverWait(self._driver, timeout)
        try:
            return wait.until(EC.invisibility_of_element_located(locator))
        except RuntimeError:
            return False

    def wait_till_alert_is_present(self, timeout=10):
        wait = WebDriverWait(self._driver, timeout)
        try:
            return wait.until(EC.alert_is_present())
        except RuntimeError:
            print("No alert")
            return False

    def get_alert_text(self, timeout=5):
        wait = WebDriverWait(self._driver, timeout)
        try:
            alert = wait.until(EC.alert_is_present())
            return alert.text
        except RuntimeError:
            return False

    def is_element_present_and_displayed(self, locator):
        """
        Check if element is present and visible. is_displayed() method still can throw NoSuchElementException
        """
        try:
            return self.find_element(*locator).is_displayed()
        except NoSuchElementException:
            return False

    def scroll_to_element(self, web_element, parameter=""):
        """
        Scroll to the exact element
        :param web_element: web element (e.g. driver.find_element_by_xpath("//div")
        :param parameter: Parameter for scroll (e.g. parameter="{block: 'center'}")
        Full list of parameters: https://developer.mozilla.org/en-US/docs/Web/API/Element/scrollIntoView
        """
        self._driver.execute_script("return arguments[0].scrollIntoView({parameter});".format(parameter=parameter),
                                    web_element)

    def scroll_to_element_center(self, element):
        """
        Scroll to the exact element
        :param element: web element (e.g. driver.find_element_by_xpath("//div")
        """
        # Calculate coordinates center of view, calculate top coordinates of retrieved element,
        # Based on these coordinates perform scroll to the top of element with
        # the down shift by half of element's height
        self.execute_script(
            "var viewPortHeight = Math.max(document.documentElement.clientHeight, window.innerHeight || 0);"
            "var elementTop = arguments[0].getBoundingClientRect().top;"
            "window.scrollBy(0, elementTop-(viewPortHeight/2));", element)
