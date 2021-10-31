import time

from selenium.webdriver.support.select import Select


class AddCustomer:
    link_customers_Menu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    link_new_customers_xpath = "// a[ @ href = '/Admin/Customer/List'] // p[contains(text(), 'Customers')]"
    btn_add_new_xpath = "//a[normalize-space()='Add new']"
    txt_email_xpath = "//input[@id='Email']"
    txt_password_xpath = "//input[@id='Password']"
    txt_firstname_xpath = "//input[@id='FirstName']"
    txt_lastname_xpath = "//input[@id='LastName']"
    rdo_male_gender_xpath = "//input[@id='Gender_Male']"
    rdo_female_gender_xpath = "//input[@id='Gender_Female']"
    btn_calendar_xpath = "//span[@class='k-icon k-i-calendar']"
    txt_dob_xpath = "//input[@id='DateOfBirth']"
    txt_companyname_xpath = "//input[@id='Company']"
    chkBox_taxexempt_xpath = "//input[@id='IsTaxExempt']"
    clrdrodown_role_xpath = "(//div[@class='k-widget k-multiselect k-multiselect-clearable'])[2]"
    dropdown_companyrole_xpath = "//li[normalize-space()='Administrators']"
    dropdown_newsletter_store_xpath = "//li[contains(text(),'Your store name')]"
    dropdown_admin_xpath = "//li[contains(text(),'Administrators')]"
    dropdown_vendor_xpath = "//li[contains(text(),'Vendors')]"
    dropdown_newsletter_teststore_xpath = "//li[contains(text(),'Test store2')]"
    dropdown_manager_of_vendor = "//select[@id='VendorId']"
    dropdown_newsletter_xpath = "(//div[@class='k-multiselect-wrap k-floatwrap'])[1]"
    chkbox_active_xpath = "//input[@id='Active']"
    btn_savebtn_xpath = "//button[@name='save']"
    txt_comment_xpath = "//textarea[@id='AdminComment']"
    success_msg_xpath = "//div[@class='alert alert-success alert-dismissable']"

    def __init__(self, driver):
        self.driver = driver

    def clickCustomerLink(self):
        self.driver.find_element_by_xpath(self.link_customers_Menu_xpath).click()

    def clickCustomerList(self):
        self.driver.find_element_by_xpath(self.link_new_customers_xpath).click()

    def btnAddNew(self):
        self.driver.find_element_by_xpath(self.btn_add_new_xpath).click()

    def enterEmail(self, email):
        self.driver.find_element_by_xpath(self.txt_email_xpath).send_keys(email)

    def enterPassword(self, password):
        self.driver.find_element_by_xpath(self.txt_password_xpath).send_keys(password)

    def enterFirstName(self, firstname):
        self.driver.find_element_by_xpath(self.txt_firstname_xpath).send_keys(firstname)

    def enterLastName(self, lastname):
        self.driver.find_element_by_xpath(self.txt_lastname_xpath).send_keys(lastname)

    def enterDob(self, dob):
        self.driver.find_element_by_xpath(self.txt_dob_xpath).click()
        self.driver.find_element_by_xpath(self.txt_dob_xpath).send_keys(dob)

    def clickGender(self, gender):
        if gender == 'Male':
            self.driver.find_element_by_xpath(self.rdo_male_gender_xpath).click()
        elif gender == 'Female':
            self.driver.find_element_by_xpath(self.rdo_female_gender_xpath).click()
        else:
            self.driver.find_element_by_xpath(self.rdo_male_gender_xpath).click()

    def enterCompanyName(self, companyname):
        self.driver.find_element_by_xpath(self.txt_companyname_xpath).send_keys(companyname)

    def clickTaxExempt(self):
        self.driver.find_element_by_xpath(self.chkBox_taxexempt_xpath).click()

    def clickActiveChBox(self):
        self.driver.find_element_by_xpath(self.chkbox_active_xpath).click()

    def selectNewsLetterDropdown(self, newsletter):
        self.driver.find_element_by_xpath(self.dropdown_newsletter_xpath).click()
        time.sleep(2)

        if newsletter == 'Your store name':
            self.listitem = self.driver.find_element_by_xpath(self.dropdown_newsletter_store_xpath)
        elif newsletter == 'Test store2':
            self.listitem = self.driver.find_element_by_xpath(self.dropdown_newsletter_teststore_xpath)

        else:
            self.listitem = self.driver.find_element_by_xpath(self.dropdown_newsletter_store_xpath)
            time.sleep(3)
            self.driver.execute_script("arguments[0].click();", self.listitem)

    def selectCustomerRole(self, role):
        time.sleep(3)
        self.driver.find_element_by_xpath(self.clrdrodown_role_xpath).click()
        time.sleep(2)
        if role == 'Administrators':
            self.listitem = self.driver.find_element_by_xpath(self.dropdown_admin_xpath)
        elif role == 'Vendors':
            self.driver.find_element_by_xpath(self.dropdown_vendor_xpath)

        else:
            self.listitem = self.driver.find_element_by_xpath(self.dropdown_admin_xpath)
            self.driver.execute_script("arguments[0].click();", self.listitem)

    def selectVendor(self, vendor):
        drop = Select(self.driver.find_element_by_xpath(self.dropdown_manager_of_vendor))
        drop.select_by_visible_text(vendor)
        print("selected vendor is:" + drop.first_selected_option.text)

    def enterComments(self, comment):
        self.driver.find_element_by_xpath(self.txt_comment_xpath).send_keys(comment)

    def clickSaveBtn(self):
        time.sleep(3)
        self.driver.execute_script("scrollBy(0,250);")
        time.sleep(2)
        self.savebtn = self.driver.find_element_by_xpath(self.btn_savebtn_xpath)
        self.driver.execute_script("arguments[0].click();", self.savebtn)
        time.sleep(5)

    def selectCalendar(self):
        date_picker = self.driver.find_element_by_xpath(self.btn_calendar_xpath)
        date_picker.click()

    def selectYear(self):
        select_Year = self.driver.find_element_by_xpath("")
