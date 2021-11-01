import time

import self
from selenium.webdriver import ActionChains


class ShoppingCartDemo:
    btn_myaccount_xpath = "//span[contains(text(),'My Account')]"
    txt_email_address_xpath = "//input[@id='input-email']"
    txt_password_xpath = "//input[@id='input-password']"
    button_login_btn = "//ul[@class='dropdown-menu dropdown-menu-right']//a[normalize-space()='Login']"
    button_submit_xpath = "//input[@value='Login']"

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self):
        self.driver.find_element_by_xpath(self.btn_myaccount_xpath).click()
        time.sleep(2)
        self.driver.find_element_by_xpath(self.button_login_btn).click()
        print('enter username')
        self.driver.find_element_by_xpath(self.txt_email_address_xpath).click()
        self.driver.find_element_by_xpath(self.txt_email_address_xpath).send_keys("automationtest@gmail.com")

    def setPassword(self):
        print('enter password')
        self.driver.find_element_by_xpath(self.txt_password_xpath).click()
        self.driver.find_element_by_xpath(self.txt_password_xpath).send_keys("test123")

    def clickSubmitBtn(self):
        print('click login btn')
        self.driver.find_element_by_xpath(self.button_submit_xpath).click()

    def validateMouseHover(self):
        actions = ActionChains(self.driver)
        desktop = self.driver.find_element_by_link_text("Desktops")
        actions.move_to_element(desktop).perform()
        time.sleep(3)
        mac = self.driver.find_element_by_link_text("Mac (1)")
        actions.move_to_element(mac).click().perform()
        print(self.driver.title)

    def validateMenuBarOptions(self):
        self.driver.find_element_by_xpath("(//a[contains(text(),'Components')])[1]").click()
        menu_options = self.driver.find_elements_by_xpath("//li[@class='dropdown open']//li")

        print('Fetch menu options')
        for options in menu_options:
            print(options.text)
            if options.text == 'Monitors (2)':
                options.click()
                print('element clicked')
                break

    def verifyAllMenuLinks(self):
        print('Fetch all links')
        all_links = self.driver.find_elements_by_xpath("//a[@class='nav-link']/p")
        print('No of links->', len(all_links))
        for items in all_links:
            print(items.text)
            print('link names->', items.text)
            print('Verify Text matches or not')
            time.sleep(5)
            if items.text == 'Product reviews':
                # time.sleep(3)
                print('Text matches')
                items.click()
                break
            time.sleep(3)
            # self.driver.implicityly_wait(5)
            print('Current page Title is >', self.driver.title)
            # break
            print('Link clicked ')
            self.driver.back()
            time.sleep(3)
            print('New page Title is >', self.driver.title)
                # break

    def clickLogout(self):
        print('Logout btn clicked ')
        self.driver.find_element_by_xpath(self.button_logout_btn).click()
