from selenium.webdriver.common.by import By

from Pages.base_page import BasePage
from controls.Input import Input


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.search_input = Input(driver=driver, placeholder="Find a course")
        self.search_btn = (By.XPATH, "search-course-button")

    def search_course(self, text):
        self.search_input.send_keys(text)
        self.driver.find_element(*self.search_btn).click()
