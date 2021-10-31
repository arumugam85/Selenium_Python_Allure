from datetime import time

import allure
import pytest
from allure_commons.types import AttachmentType

from pageObjects.AddProducts import AddProducts
from pageObjects.LoginPage import LoginPage
from pageObjects.ShoppingCartDemo import ShoppingCartDemo
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_007_ShoppingCart:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @allure.description("**********Validate NOP commerce application with login credentials**********")
    @allure.severity(severity_level="CRITICAL")
    def test_login(self, setup):

        self.logger.info("****Started Login Test****")
        self.driver = setup
        self.driver.get("http://tutorialsninja.com/demo")
        self.lp = ShoppingCartDemo(self.driver)
        self.lp.setUserName()
        self.lp.setPassword()
        self.lp.clickSubmitBtn()
        self.lp.validateMouseHover()
        self.lp.validateMenuBarOptions()

