import datetime

import pytest
from selenium import webdriver
from webdriver_manager import driver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        # driver = webdriver.Chrome()
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()

    elif browser == 'firefox':
        driver = webdriver.Firefox()
        driver.maximize_window()

    return driver


def teardown(self):
    if driver is None:
        self.logger.info("***********Test is Destroyed*************")
        self.logger.info("Test destroyed at "+str(datetime.datetime.now()))
        driver.close()
        driver.quit()


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


def pytest_configure(config):
    config._metadata['Project Name'] = 'ECommerce Application'
    config._metadata['Framework'] = 'PyTest Framework'
    config._metadata['Language'] = 'Python'
    config._metadata['Author'] = 'Aru'
