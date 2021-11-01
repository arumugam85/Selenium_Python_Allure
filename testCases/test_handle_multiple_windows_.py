import time
import allure
import pytest
from selenium import webdriver
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

    @allure.description("**********Validate handling multiple window**********")
    @allure.severity(severity_level="CRITICAL")
    def test_alertWindow(self, test_setup):
        self.logger.info("****Started Login Test****")
        #self.driver = setup
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        time.sleep(3)
        print('Title->', self.driver.title)
        self.driver.execute_script("window.scrollTo(0, 1000);")
        parent_Window = self.driver.current_window_handle
        print('Parent Window ->', parent_Window)
        self.driver.find_element_by_css_selector(
            "div:nth-child(1) div:nth-child(6) div:nth-child(2) a:nth-child(1) > img:nth-child(1)").click()
        child_windows = self.driver.window_handles
        print('Child Window->', child_windows)

        for child in child_windows:
            if parent_Window != child:
                self.driver.switch_to.window(child)
                print('Title->', self.driver.title)
                self.driver.find_element_by_xpath("//input[@id='email-address']").send_keys("Admin")
                self.driver.find_element_by_xpath("//input[@id='password']").send_keys("admin123")
                print('Title->', self.driver.title)
                self.driver.close()

        self.driver.switch_to.window(parent_Window)
        print('Parent Window ->', parent_Window)
        time.sleep(3)
        print('Title->', self.driver.title)
        self.driver.find_element_by_xpath("//input[@id='txtUsername']").send_keys("Admin")
        self.driver.find_element_by_xpath("//input[@id='txtPassword']").send_keys("admin123")
        self.driver.find_element_by_xpath("//input[@id='btnLogin']").click()
