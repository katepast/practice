import datetime
import pytest
from selenium import webdriver

from configs.config import COURSES_URL
from practice_page.Pages.base_page import BasePage


@pytest.fixture()
def browser(request):
    path = '/Users/kate.pastbina/PycharmProjects/practice/practice_page/driver/chromedriver'
    driver =\
        webdriver.Chrome(executable_path=path)
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
    base_page.open_url()
    yield browser


@pytest.fixture()
def open_course_site(browser):
    base_page = BasePage(browser)
    base_page.open_url(url=COURSES_URL)
    yield browser






