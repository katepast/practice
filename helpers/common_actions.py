from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CommonActions:

    @staticmethod
    def wait_till_element_present(driver, locator, timeout=10):
        wait = WebDriverWait(driver, timeout)
        try:
            return wait.until(EC.element_to_be_clickable(locator))
        except RuntimeError:
            return False

    @staticmethod
    def wait_till_text_present(driver, locator, text, timeout=10):
        wait = WebDriverWait(driver, timeout)
        try:
            return wait.until(EC.text_to_be_present_in_element(locator, text))
        except RuntimeError:
            return False

    @staticmethod
    def wait_till_element_checked(driver, locator, timeout=10):
        wait = WebDriverWait(driver, timeout)
        try:
            return wait.until(EC.element_to_be_selected(locator))
        except RuntimeError:
            return False

    @staticmethod
    def wait_till_element_presents(driver, locator, timeout=10):
        wait = WebDriverWait(driver, timeout)
        try:
            return wait.until(EC.presence_of_all_elements_located(locator))
        except RuntimeError:
            return False

    @staticmethod
    def wait_till_element_not_visible(driver, locator, timeout=10):
        wait = WebDriverWait(driver, timeout)
        try:
            return wait.until(EC.invisibility_of_element_located(locator))
        except RuntimeError:
            return False

    @staticmethod
    def wait_till_alert_is_present(driver, timeout=10):
        wait = WebDriverWait(driver, timeout)
        try:
            return wait.until(EC.alert_is_present())
        except RuntimeError:
            print("No alert")
            return False

    @staticmethod
    def get_alert_text(driver, timeout=5):
        wait = WebDriverWait(driver, timeout)
        try:
            alert = wait.until(EC.alert_is_present())
            return alert.text
        except RuntimeError:
            return False

