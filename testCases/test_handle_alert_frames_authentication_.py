import time

import allure
import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class Test_008_MouseActions:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.fixture()
    def test_setup(self):
        global driver
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        yield
        self.driver.quit()

    @allure.description("**********Validate Alert pop up window**********")
    @allure.severity(severity_level="CRITICAL")
    def test_alertWindow(self, test_setup):
        self.logger.info("****Started Login Test****")
        #self.driver = setup
        self.driver.get("https://mail.rediff.com/cgi-bin/login.cgi")
        self.driver.find_element_by_xpath("//input[@name='proceed']").click()
        time.sleep(3)
        alert = self.driver.switch_to_alert()
        print(alert.text)
        alert.accept()

    @allure.description("**********Validate Authentication window**********")
    @allure.severity(severity_level="CRITICAL")
    def test_loginAuthentication(self, setup):
        self.logger.info("****Started Login Test****")
        self.driver = setup
        self.driver.get("http://admin:admin@the-internet.herokuapp.com/basic_auth")
        print(self.driver.title)

    @allure.description("**********Validate frames window**********")
    @allure.severity(severity_level="CRITICAL")
    def test_frames(self, setup):
        self.logger.info("****Started Login Test****")
        self.driver = setup
        self.driver.get("https://www.redbus.in/")
        self.driver.find_element_by_xpath("//i[@id='i-icon-profile']").click()
        self.driver.find_element_by_xpath("//li[@id='signInLink']").click()
        print('switch to frame window')
        self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@class='modalIframe']"))
        self.driver.find_element_by_xpath("//input[@id='mobileNoInp']").click()
        print('enter phone number')
        self.driver.find_element_by_xpath("//input[@id='mobileNoInp']").send_keys("98400690123")
        time.sleep(3)
        self.driver.switch_to.parent_frame()
        self.driver.switch_to.default_content()
        print('back to parent frame')


