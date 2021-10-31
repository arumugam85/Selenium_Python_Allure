import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class AddDiscount:
    link_promotion_css = ".has-treeview:nth-child(5) > .nav-link > p"
    link_discount_xpath = "//p[contains(.,'Discounts')]"
    btn_addNew_xpath = "//a[normalize-space()='Add new']"
    txt_discount_name_css = "#Name"
    drp_discount_type_css = "#DiscountTypeId"
    txt_discount_amt_xpath = "(//input[@class='k-formatted-value k-input'])[3]"
    txt_start_date_css = "#StartDateUtc"
    txt_end_date_css = "#EndDateUtc"
    drp_discount_limit_css = "#DiscountLimitationId"
    btn_save_xpath = "//button[@name='save']"
    chkBox_percent_xpath = "//input[@id='UsePercentage']"
    select_discount_type_xpath = "//select[@id='SearchDiscountTypeId']"
    txt_search_discount_name_css = "#SearchDiscountName"
    btn_search_xpath = "//button[@id='search-discounts']"
    btn_logout_xpath = "//a[normalize-space()='Logout']"
    txt_discount_type_css = "tr[class='odd'] td:nth-child(2)"

    def __init__(self, driver):
        self.driver = driver

    def clickPromotionLink(self):
        try:
            self.driver.find_element_by_css_selector(self.link_promotion_css).click()
        except Exception as e:
            print("Promotion link is not clickable")

    def clickDiscountLink(self):
        try:
            self.driver.find_element_by_xpath(self.link_discount_xpath).click()
        except Exception as e:
            print("Element is not clickable")

    def clickAddNew(self):
        try:
            self.driver.find_element_by_xpath(self.btn_addNew_xpath).click()
        except Exception as e:
            print("Element is not clickable")

    def enterDiscountName(self, discount_name):
        self.driver.find_element_by_css_selector(self.txt_discount_name_css).send_keys(discount_name)

    def selectDiscountType(self, discount_type):
        time.sleep(3)
        print("select dropdown for discount type")
        self.driver.find_element_by_css_selector(self.drp_discount_type_css).click()
        time.sleep(2)
        element = self.driver.find_element_by_css_selector(self.drp_discount_type_css)
        drop = Select(element)
        # drop.select_by_index(2)
        time.sleep(2)
        drop.select_by_visible_text(discount_type)
        print("dropdown selected for discount values")

    def enterDiscountAmount(self, discount_amt):

        try:
            WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "(//input[@class='k-formatted-value k-input'])[3]"))).click()
            time.sleep(3)
            print("enter discount amount value")
            amount = self.driver.find_element_by_css_selector("#DiscountAmount")
            amount.send_keys(discount_amt)

        except Exception as e:
            print("failed to enter discount amount")

    def enterStartDate(self, start_date):

        self.driver.find_element_by_css_selector(self.txt_start_date_css).send_keys(start_date)

    def enterEndDate(self, end_date):
        self.driver.find_element_by_css_selector(self.txt_end_date_css).send_keys(end_date)

    def selectDiscountLimit(self, discount_limit):
        time.sleep(3)
        print("enter discount amount limit")
        selectDiscount = Select(self.driver.find_element_by_css_selector(self.drp_discount_limit_css))
        selectDiscount.select_by_visible_text(discount_limit)

    def clickSaveBtn(self):
        time.sleep(2)
        self.driver.find_element_by_xpath(self.btn_save_xpath).click()

    def searchDiscountType(self, search_discount_type):
        time.sleep(3)
        print("select discount type")
        dropdown1 = Select(self.driver.find_element_by_xpath(self.select_discount_type_xpath))
        dropdown1.select_by_visible_text(search_discount_type)

    def enterSearchDiscountName(self, search_discount_name):
        self.driver.find_element_by_css_selector(self.txt_search_discount_name_css).click()
        self.driver.find_element_by_css_selector(self.txt_search_discount_name_css).send_keys(search_discount_name)

    def clickSearchBtn(self):
        time.sleep(2)
        self.driver.find_element_by_xpath(self.btn_search_xpath).click()

    def clickLogOutBtn(self):
        time.sleep(2)
        self.driver.find_element_by_xpath(self.btn_logout_xpath).click()

    def verifyDiscountTypeText(self, search_discount_type):
        time.sleep(3)
        discount_type = self.driver.find_element_by_css_selector(self.txt_discount_type_css)
        print("Actual Text ->", discount_type.text)
        print("Expected Text ->", search_discount_type)

        if discount_type.text == search_discount_type:
            # self.logger.info("**** Search discount type passed ****")
            print('Text matches passed')
            #self.driver.close()
            assert True
        else:
            # self.logger.error("**** Search discount type failed ****")
            print('Text matches Failed')
            self.driver.save_screenshot(".\\Screenshots\\" + "test_disocuntType.png")
            #self.driver.close()
            assert False
