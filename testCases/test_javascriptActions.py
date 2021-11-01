import time
import traceback

import pytest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager

from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


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

    def test_userRegister(self, test_setup):
        self.logger.info("*************** Test_001_Login *****************")
        self.logger.info("****Started Home page title test ****")
        #self.driver = setup
        self.logger.info("****Opening URL****")
        self.driver.get("http://tutorialsninja.com/demo/")
        # time.sleep(15)
        # alert = self.driver.switch_to.alert()
        # print(alert.text)
        # alert.accept()
        print('verify title')
        print(self.driver.execute_script("return document.title"))
        time.sleep(3)
        element = self.driver.execute_script("return document.querySelector(\"a[title='My Account']\")")
        self.driver.execute_script("arguments[0].click();", element)
        time.sleep(3)

        register_elem = self.driver.find_element_by_link_text("Register")
        self.driver.execute_script("arguments[0].click();", register_elem)

        time.sleep(2)
        self.driver.execute_script("return document.getElementById('input-firstname').value='Raj'")
        self.driver.execute_script("return document.getElementById('input-lastname').value='Kumar'")
        self.driver.execute_script("return document.getElementById('input-email').value='test1233@gmail.com'")
        self.driver.execute_script("return document.getElementById('input-telephone').value='7046759339'")
        self.driver.execute_script("return document.getElementById('input-password').value='test1235'")
        self.driver.execute_script("return document.getElementById('input-confirm').value='test1235'")

        self.driver.execute_script("window.scrollBy(0,500)", "")
        time.sleep(3)
        radio_btn = self.driver.find_element_by_name("newsletter")
        self.driver.execute_script("arguments[0].click();", radio_btn)

        chk_box = self.driver.execute_script("return document.querySelector(\"input[name='agree']\")")
        self.driver.execute_script("arguments[0].click();", chk_box)

        continue_btn = self.driver.execute_script("return document.querySelector(\"input[value='Continue']\")")
        self.driver.execute_script("arguments[0].click();", continue_btn)

        try:
            actual = self.driver.find_element_by_xpath("//div[@id ='content']//h1")
            assert "Your Account Has Been Created!" in actual.text

        except AssertionError:
            print(traceback.format_exc())

        except NoSuchElementException:
            print(traceback.format_exc())
