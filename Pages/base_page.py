from selenium.webdriver.common.by import By
from configs.config import BASE_URL
from conftest import WebDriver


class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.login_btn_link = (By.LINK_TEXT, './/a[normalize-space(.)="Login"]')
        self.practice_btn_link = (By.XPATH, './/a[normalize-space(.)="Practice"]')

    def open_url(self, url: str = BASE_URL):
        self.driver.get(url)
