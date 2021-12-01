from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
# from Pages.login_page import LoginPage
# from Pages.practice_page import PracticePage


class BasePage:
    BASE_URL = "https://courses.letskodeit.com/practice"
    COURSES_URL = "https://courses.letskodeit.com/courses"

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.login_btn_link = (By.LINK_TEXT, './/a[normalize-space(.)="Login"]')
        self.practice_btn_link = (By.XPATH, './/a[normalize-space(.)="Practice"]')

    def open_url(self, url: str = BASE_URL):
        self.driver.get(url)

    # def open_login_page(self):
    #     self.driver.find_element(*self.login_btn_link).click()
    #     return LoginPage(self.driver)
    #
    # def open_practice_page(self):
    #     self.driver.find_element(*self.practice_btn_link).click()
    #     return PracticePage(self.driver)
