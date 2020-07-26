from selenium.webdriver.common.by import By

from Pages.base_page import BasePage
from Pages.main_page import MainPage
from controls.Input import Input
from helpers.config import Data


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.email_input = Input(driver=driver, locator=(By.ID, "user_email"))
        self.password_input = Input(driver=driver, locator=(By.ID, "user_password"))
        self.login_btn = Input(driver, locator=(By.XPATH, ".//input[@type='submit']"))

    def set_login_credentials(self, email=Data.EMAIL.value, password=Data.PASSWORD.value):
        self.email_input.send_keys(email)
        self.password_input.send_keys(password)

    def click_login_btn(self):
        self.login_btn.click()
        return MainPage(self.driver)
