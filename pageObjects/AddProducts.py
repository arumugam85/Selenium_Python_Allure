import time
from telnetlib import EC

from selenium.webdriver import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import select
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager import driver


class AddProducts:
    lnk_catelog_xpath = "//p[normalize-space()='Catalog']"
    lnk_products_xpath = "//p[normalize-space()='Products']"
    btn_addnew_xpath = "//i[@class='fas fa-plus-square']"
    txt_prod_name_xpath = "//input[@id='Name']"
    txt_short_desc_xpath = "//textarea[@id='ShortDescription']"
    txt_sku_xpath = "//input[@id='Sku']"
    drp_category_xpath = "(//div[@role='listbox'])[1]"
    drp_category_value_css = "select[id='SelectedCategoryIds'] option[value='1']"
    drp_mfg_css = "div[class='k-widget k-multiselect k-multiselect-clearable k-state-hover'] div[role='listbox']"
    txt_prod_tags_xpath = "//div[contains(text(),'Enter tags ...')]"
    txt_gtin_xpath = "//input[@id='Gtin']"
    txt_mfg_part_no_xpath = "//input[@id='ManufacturerPartNumber']"
    drp_prod_type_css = "#ProductTypeId"
    drp_prod_temp_xpath = "//select[@id='ProductTemplateId']"
    drp_custrole_xpath = "(//div[@class='k-widget k-multiselect k-multiselect-clearable'])[3]"
    txt_startdate_xpath = "//input[@id='AvailableStartDateTimeUtc']"
    txt_enddate_xpath = "//input[@id='AvailableEndDateTimeUtc']"
    btn_save_xpath = "//button[@name='save']"

    def __init__(self, driver):
        self.driver = driver

    def clickCategoryLink(self):
        self.driver.find_element_by_xpath(self.lnk_catelog_xpath).click()

    def clickProductsLink(self):
        self.driver.find_element_by_xpath(self.lnk_products_xpath).click()

    def clickAddNewBtn(self):
        self.driver.find_element_by_xpath(self.btn_addnew_xpath).click()

    def enterProductName(self, prod_name):
        self.driver.find_element_by_xpath(self.txt_prod_name_xpath).send_keys(prod_name)

    def enterProductDesc(self, prod_desc):
        self.driver.find_element_by_xpath(self.txt_short_desc_xpath).send_keys(prod_desc)

    def enterSKUName(self, sku_name):
        self.driver.find_element_by_xpath(self.txt_sku_xpath).send_keys(sku_name)

    def selectCategories(self, category_name):
        time.sleep(10)
        # self.driver.find_element_by_xpath(self.drp_category_xpath).send_keys(category_name)
        print("select category menu from list")

        try:
            self.driver.find_element_by_xpath("(//div[@role='listbox'])[1]").click()
            time.sleep(3)
            self.driver.find_element_by_xpath("//li[normalize-space()='Computers']").click()
            # select.select_by_visible_text("Computers")
            print("dropdown value selected successfully")
        except Exception as e:
            print("dropdown value is not clickable")

        # time.sleep(5)
        # select = self.driver.find_element_by_xpath(self.drp_category_xpath)
        # print("select category value from list")
        # category.send_keys("Computers")
        # select.select_by_value("Computers")
        # print("Selected item ->" + category.first_selected_option.text)

    def selectManufacturingName(self, mfg_name):
        # self.driver.find_element_by_xpath(self.drp_mfg_xpath).send_keys(mfg_name)
        mfg = self.driver.find_element_by_css_selector(self.drp_mfg_css)
        drp = Select(mfg).select_by_visible_text(mfg_name)

    def enterProductTagName(self, prod_tagname):

        self.driver.find_element_by_xpath(self.txt_prod_tags_xpath).click()
        print("Enter prod tag name")
        self.driver.find_element_by_xpath("//input[@class='ui-autocomplete-input']").send_keys(prod_tagname)

    def enterGTINNumber(self, gtin_number):
        self.driver.find_element_by_xpath(self.txt_gtin_xpath).send_keys(gtin_number)

    def enterMFGNumber(self, mfg_number):
        self.driver.find_element_by_xpath(self.txt_mfg_part_no_xpath).send_keys(mfg_number)

    def selectProdType(self, prod_type):
        # self.driver.find_element_by_xpath(self.drp_prod_type_xpath).send_keys(prod_type)
        prodtype = self.driver.find_element_by_css_selector(self.drp_prod_type_css)
        drp = Select(prodtype).select_by_visible_text(prod_type)

    def enterProdTemplate(self, prod_template):
        self.driver.find_element_by_xpath(self.drp_prod_temp_xpath).send_keys(prod_template)

    def selectCustRoles(self, cust_role):
        print("select customer role")
        self.driver.find_element_by_xpath(self.drp_custrole_xpath).click()
        self.driver.find_element_by_xpath("//li[normalize-space()='Administrators']").click()
        print("customer role selected successfully")

    def enterStartDate(self, start_date):
        print("select start date")
        self.driver.find_element_by_xpath(self.txt_startdate_xpath).click()
        self.driver.find_element_by_xpath(self.txt_startdate_xpath).send_keys(start_date)

    def enterEndDate(self, end_date):
        print("select end date")
        self.driver.find_element_by_xpath(self.txt_enddate_xpath).click()
        self.driver.find_element_by_xpath(self.txt_enddate_xpath).send_keys(end_date)

    def clickSaveBtn(self):
        self.driver.find_element_by_xpath(self.btn_save_xpath).click()
        print("Save btn clicked")
