import time
import pytest
import os
from selenium import webdriver

from configs.config import COURSES_URL
from helpers.web_driver.practice_web_driver import WebDriver, WebDriverListener
from project_const import chromedriver_path, screenshot_path
from Pages.base_page import BasePage


@pytest.fixture()
def browser(request):
    driver = webdriver.Chrome(executable_path=chromedriver_path)
    ef_driver = WebDriver(driver, WebDriverListener())
    ef_driver.maximize_window()
    failed_before = request.session.testsfailed
    yield ef_driver
    if request.session.testsfailed != failed_before:
        if not os.path.exists(screenshot_path):
            os.mkdir("practice_page/screenshot")
        ef_driver.save_screenshot(screenshot_path + "/screen_%s.png" % (time.asctime()))
    ef_driver.quit()


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






