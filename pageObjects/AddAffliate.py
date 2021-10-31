import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager import driver


class AddAffliate:
    btn_affliate_xpath = "//p[normalize-space()='Affiliates']"
    btn_addnew_xpath = "//a[normalize-space()='Add new']"
    txt_firstName_xpath = "//input[@id='Address_FirstName']"
    txt_lastName_xpath = "//input[@id='Address_LastName']"
    txt_email_xpath = "//input[@id='Address_Email']"
    txt_company_xpath = "//input[@id='Address_Company']"
    drp_country_xpath = "//select[@id='Address_CountryId']"
    drp_state_css = "#Address_StateProvinceId"
    txt_region_xpath = "//input[@id='Address_County']"
    txt_city_xpath = "//input[@id='Address_City']"
    txt_address_xpath = "//input[@id='Address_Address1']"
    txt_zipcode_xpath = "//input[@id='Address_ZipPostalCode']"
    txt_phone_xpath = "//input[@id='Address_PhoneNumber']"
    txt_fax_xpath = "//input[@id='Address_FaxNumber']"
    btn_save_xpath = "//button[@name='save']"
    btn_edit_affliate = "//i[@class='fas fa-pencil-alt']"
    txt_edit_company_css = "#Address_Company"
    btn_delete = "//span[@id='affiliate-delete']"
    btn_confirm_delete = "//button[normalize-space()='Delete']"
    txt_update_success_msg = "//div[@class='alert alert-success alert-dismissable']"

    def __init__(self, driver):
        self.driver = driver;

    def clickAffliate(self):
        self.driver.find_element_by_xpath(self.btn_affliate_xpath).click()

    def clickAddNewBtn(self):
        self.driver.find_element_by_xpath(self.btn_addnew_xpath).click()

    def enterFirstName(self, first_name):
        self.driver.find_element_by_xpath(self.txt_firstName_xpath).send_keys(first_name)

    def enterLastName(self, last_name):
        self.driver.find_element_by_xpath(self.txt_lastName_xpath).send_keys(last_name)

    def enterEmail(self, email):
        self.driver.find_element_by_xpath(self.txt_email_xpath).send_keys(email)

    def enterCompanyName(self, company_name):
        self.driver.find_element_by_xpath(self.txt_company_xpath).send_keys(company_name)

    def selectCountry(self, country_name):
        selectCountry = Select(self.driver.find_element_by_xpath(self.drp_country_xpath))
        selectCountry.select_by_visible_text(country_name)
        time.sleep(5)

    def selectState(self, state_name):
        time.sleep(5)
        state = self.driver.find_element_by_css_selector(self.drp_state_css)
        drp = Select(state).select_by_visible_text(state_name)
        time.sleep(3)


    def enterCounty(self, region_name):
        self.driver.find_element_by_xpath(self.txt_region_xpath).send_keys(region_name)

    def enterCityName(self, city_name):
        self.driver.find_element_by_xpath(self.txt_city_xpath).send_keys(city_name)

    def enterAddress(self, address):
        self.driver.find_element_by_xpath(self.txt_address_xpath).send_keys(address)

    def enterZipCode(self, zip_code):
        self.driver.find_element_by_xpath(self.txt_zipcode_xpath).send_keys(zip_code)

    def enterPhoneNumber(self, phone_number):
        self.driver.find_element_by_xpath(self.txt_phone_xpath).send_keys(phone_number)

    def enterFaxNumber(self, fax_number):
        self.driver.find_element_by_xpath(self.txt_fax_xpath).send_keys(fax_number)

    def clickSaveBtn(self):
        self.driver.find_element_by_xpath(self.btn_save_xpath).click()

    def clickEditButton(self):
        self.driver.find_element_by_xpath(self.btn_edit_affliate).click()

    def editCompanyName(self, comp_name):
        self.driver.find_element_by_css_selector(self.txt_edit_company_css).clear()
        self.driver.find_element_by_css_selector(self.txt_edit_company_css).send_keys(comp_name)

    def clickDeleteButton(self):
        self.driver.find_element_by_xpath(self.btn_delete).click()
        time.sleep(5)
        self.driver.find_element_by_xpath(self.btn_confirm_delete).click()

    def verifySuccessMsg(self):
        time.sleep(3)
        self.expText = "The new affiliate has been added successfully."
        self.actText = self.driver.find_element_by_xpath(self.txt_update_success_msg).text
        print("actual msg is:", self.actText)
        #self.assertEqual(expText, actText)
