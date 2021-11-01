from datetime import time

import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from pageObjects.AddProducts import AddProducts
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Login:
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

    # @pytest.mark.regression
    def test_homePageTitle(self, test_setup):
        self.logger.info("*************** Test_001_Login *****************")
        self.logger.info("****Started Home page title test ****")
        #self.driver = setup
        self.logger.info("****Opening URL****")
        self.driver.get(self.baseURL)
        self.logger.info("***********Test is Destroyed*************")
        act_title = self.driver.title

        if act_title == "Your store. Login":
            self.logger.info("**** Home page title test passed ****")
            self.driver.close()
            assert True
        else:
            self.logger.error("**** Home page title test failed ****")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
            self.driver.close()
            assert False

    # @pytest.mark.sanity
    # @pytest.mark.regression
    @allure.description("**********Validate NOP commerce application with login credentials**********")
    @allure.severity(severity_level="CRITICAL")
    def test_login(self, setup):

        self.logger.info("****Started Login Test****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.products = AddProducts(self.driver)
        self.products.clickCategoryLink()
        self.lp.verifyAllMenuLinks()
        self.lp.clickBackBtn()
        act_title = self.driver.title
        print('verify page title', act_title)

        if act_title == 'Dashboard / nopCommerce administration':
            self.logger.info("****Login test passed ****")
            allure.attach(self.driver.get_screenshot_as_png(), name="testloginscreen",
                          attachment_type=AttachmentType.PNG)
            self.driver.close()
            assert True
        else:
            self.logger.error("****Login test failed ****")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="testloginscreen",
                          attachment_type=AttachmentType.PNG)
            self.driver.close()
            assert False
