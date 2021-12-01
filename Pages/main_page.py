from selenium.webdriver.common.by import By

from helpers.common_actions import CommonActions
from helpers.logging import logger
from practice_page.Pages.base_page import BasePage
from practice_page.controls.Input import Input


class CoursePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.search_input = Input(driver=driver, placeholder="Search Course")
        self.search_btn = (By.XPATH, ".//button[contains(@class, 'search-course')]")
        self.source_icon = By.XPATH, ".//h4[@class='dynamic-heading']"
        self.all_courses_title =\
            By.XPATH, ".//h1[contains(@class,'dynamic-heading') and normalize-space()='All Courses']"

    def search_course(self, text):
        """
        Method to search specified course item
        """
        logger.debug("Search specified course item")
        self.search_input.set_value(text)
        self.driver.find_element(*self.search_btn).click()

    def is_course_link_url_displayed(self):
        """
        Method to check presence of presence of title 'All Courses' on the page
        """
        logger.debug("Check presence of presence of title 'All Courses' on the page")
        return CommonActions.wait_till_element_is_displayed(self.driver, self.all_courses_title)

    def get_all_items(self):
        """
        Method to receive all founded items on the grid list
        :return: list of searched items
        """
        logger.debug("Receive all founded items on the grid list")
        items_in_context_menu = self.driver.find_elements(*self.source_icon)
        return [el.text for el in items_in_context_menu if el.text]
