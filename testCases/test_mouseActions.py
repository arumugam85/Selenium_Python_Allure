from datetime import time

import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

from pageObjects.AddProducts import AddProducts
from pageObjects.LoginPage import LoginPage
from pageObjects.ShoppingCartDemo import ShoppingCartDemo
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


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
    @allure.description("**********Validate NOP commerce application with login credentials**********")
    @allure.severity(severity_level="CRITICAL")
    def test_login(self, test_setup):
        self.logger.info("****Started Login Test****")
        #self.driver = setup
        self.driver.get("https://jqueryui.com/resources/demos/droppable/default.html")

        source = self.driver.find_element_by_id("draggable")
        target = self.driver.find_element_by_id("droppable")

        actions = ActionChains(self.driver)
        actions.click_and_hold(source).move_to_element(target).release().perform()
        print("Mosue drap n drop worked")
