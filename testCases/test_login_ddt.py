import time

import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from pageObjects.LoginPage import LoginPage
from utilities import XLUtils
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class Test_002_DDT_Login:
    baseURL = ReadConfig.getApplicationURL()
    path = ".//TestData/InputData.xlsx"
    logger = LogGen.loggen()  # Logger

    @pytest.fixture()
    def test_setup(self):
        global driver
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        yield
        self.driver.quit()

    def test_login_ddt(self, test_setup):
        self.logger.info("******* Starting Test_002_DDT_Login Test **********")
        self.logger.info("******* Starting Login DDT Test **********")
        ss_path = "/test_login/"
        # ss = ScreenShots(self.driver)
        #self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)

        self.rows = XLUtils.getRowCount(self.path, 'login')
        print('Number of rows...', self.rows)
        lst_status = []

        for r in range(2, self.rows + 1):
            self.user = XLUtils.readData(self.path, 'login', r, 1)
            self.password = XLUtils.readData(self.path, 'login', r, 2)
            self.exp = XLUtils.readData(self.path, 'login', r, 3)

            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.exp == 'Pass':
                    self.logger.info("**** passed ****")
                    self.lp.clickLogout();
                    lst_status.append("Pass")
                    # ss.Screenshot(ss_path + "login.png")
                    allure.attach(self.driver.get_screenshot_as_png(), name="testloginscreen",
                                  attachment_type=AttachmentType.PNG)
                elif self.exp == 'Fail':
                    self.logger.info("**** failed ****")
                    allure.attach(self.driver.get_screenshot_as_png(), name="testloginscreen",
                                  attachment_type=AttachmentType.PNG)
                    self.lp.clickLogout();
                    lst_status.append("Fail")

            elif act_title != exp_title:
                if self.exp == 'Pass':
                    self.logger.info("**** failed ****")
                    lst_status.append("Fail")
                elif self.exp == 'Fail':
                    self.logger.info("**** passed ****")
                    lst_status.append("Pass")
            print(lst_status)
        if "Fail" not in lst_status:
            self.logger.info("******* DDT Login test passed **********")
            self.driver.close()
            assert True
        else:
            self.logger.error("******* DDT Login test failed **********")
            self.driver.close()
            assert False

        self.logger.info("******* End of Login DDT Test **********")
        self.logger.info("**************** Completed  TC_LoginDDT_002 ************* ");
