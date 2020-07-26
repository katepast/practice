import datetime
import pytest
from selenium import webdriver

from Pages.base_page import BasePage


@pytest.fixture()
def browser():
    driver = webdriver.Chrome(executable_path='/Users/Kate/PycharmProjects/AQA/driver/chromedriver 2')
    driver.maximize_window()
    yield driver
    driver.save_screenshot("/Users/Kate/PycharmProjects/AQA/screenshots/screenschot_%s.png" % (datetime.datetime.now()))
    driver.quit()


@pytest.fixture()
def open_site(browser):
    base_page = BasePage(browser)
    base_page.open()
    yield browser

#
# @pytest.fixture()
# def open_login_page(open_site):
#     login_page = LoginPage(open_site)
#     login_page.open_login_page()
#     login_page.set_login_credentials()
#     login_page.click_login_btn()
#     yield open_site


# @pytest.fixture()
# def login_to_site(open_login_page):
#     login_page = LoginPage(open_login_page)
#     login_page.set_login_credentials()
#     login_page.click_login_btn()
#     yield open_site





