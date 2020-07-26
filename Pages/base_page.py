from selenium.webdriver.common.by import By
# from Pages.login_page import LoginPage
# from Pages.practice_page import PracticePage


class BasePage:
    BASE_URL = "https://learn.letskodeit.com/p/practice"

    def __init__(self, driver):
        self.driver = driver
        self.login_btn_link = (By.LINK_TEXT, './/a[normalize-space(.)="Login"]')
        self.practice_btn_link = (By.XPATH, './/a[normalize-space(.)="Practice"]')

    def open(self):
        self.driver.get(self.BASE_URL)

    # def open_login_page(self):
    #     self.driver.find_element(*self.login_btn_link).click()
    #     return LoginPage(self.driver)
    #
    # def open_practice_page(self):
    #     self.driver.find_element(*self.practice_btn_link).click()
    #     return PracticePage(self.driver)
