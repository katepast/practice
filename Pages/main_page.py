from selenium.webdriver.common.by import By

from controls.dummy_control import DummyControl
from helpers.common_actions import CommonActions
from practice_page.Pages.base_page import BasePage
from practice_page.controls.Input import Input


class CoursePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.search_input = Input(driver=driver, placeholder="Search Course")
        self.search_btn = (By.XPATH, ".//button[contains(@class, 'search-course')]")
        self.source_icon = By.XPATH, ".//h4[@class='dynamic-heading']"

    def search_course(self, text):
        self.search_input.set_value(text)
        self.driver.find_element(*self.search_btn).click()

    def get_all_items(self):
        items_in_context_menu = self.driver.find_elements(*self.source_icon)
        return [el.text for el in items_in_context_menu if el.text]
