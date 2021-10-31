import time


class LoginPage:
    txt_email_address_id = "Email"
    txt_password_id = "Password"
    button_login_btn = "//button[@class='button-1 login-button']"
    button_logout_btn = "(//a[@class='nav-link'])[2]"

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        print('enter username')
        self.driver.find_element_by_id(self.txt_email_address_id).clear()
        self.driver.find_element_by_id(self.txt_email_address_id).send_keys(username)

    def setPassword(self, password):
        print('enter password')
        self.driver.find_element_by_id(self.txt_password_id).clear()
        self.driver.find_element_by_id(self.txt_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element_by_xpath(self.button_login_btn).click()

    def verifyAllMenuLinks(self):
        print('Fetch all links')
        all_links = self.driver.find_elements_by_xpath("//a[@class='nav-link']/p")
        print('No of links->', len(all_links))
        for items in all_links:
            print(items.text)
            print('link names->', items.text)
            print('Verify Text matches or not')
            time.sleep(5)
            if (items.text == 'Product reviews'):
            # time.sleep(3)
                print('Text matches')
                items.click()
                time.sleep(3)
            # self.driver.implicityly_wait(5)
                print('Current page Title is >', self.driver.title)
                #break
                print('Link clicked ')
                self.driver.back()
                time.sleep(3)
                print('New page Title is >', self.driver.title)
                #break

    def clickLogout(self):
        print('Logout btn clicked ')
        self.driver.find_element_by_xpath(self.button_logout_btn).click()
