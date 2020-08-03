import datetime
import pytest
from selenium import webdriver

from Pages.base_page import BasePage
from Pages.login_page import LoginPage


@pytest.fixture()
def browser(request):
    driver = webdriver.Chrome(executable_path='/Users/Kate/PycharmProjects/PracticePageAQA/driver/chromedriver 2')
    driver.maximize_window()
    failed_before = request.session.testsfailed
    yield driver
    if request.session.testsfailed != failed_before:
        driver.save_screenshot("/Users/Kate/PycharmProjects/PracticePageAQA/screenshots/screenschot_%s.png" %
                               (datetime.datetime.now()))
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
#     login_page.set_login_credentials()
#     login_page.click_login_btn()
#     yield open_site


# @pytest.fixture()
# def login_to_site(open_login_page):
#     login_page = LoginPage(open_login_page)
#     login_page.set_login_credentials()
#     login_page.click_login_btn()
#     yield open_site





