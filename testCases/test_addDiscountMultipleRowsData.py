import time

import pytest
import self
import xlrd
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from pageObjects.AddDiscount import AddDiscount
from pageObjects.LoginPage import LoginPage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig

## Read data from config files
self.baseURL = ReadConfig.getApplicationURL()
self.username = ReadConfig.getUsername()
self.password = ReadConfig.getPassword()
self.logger = LogGen.loggen()


@pytest.fixture()
def test_setup(self):
    global driver
    self.driver = webdriver.Chrome(ChromeDriverManager().install())
    self.driver.implicitly_wait(10)
    self.driver.maximize_window()
    yield
    self.driver.quit()

self.driver = webdriver.Chrome(ChromeDriverManager().install())
self.driver.implicitly_wait(10)

print('Launch Nop commerce application')
# self.driver.get("https://admin-demo.nopcommerce.com/Admin")
self.driver.get(self.baseURL)
self.driver.maximize_window()

## Create Workbook sheet
path = ".//TestData/InputData.xlsx"
workbook = xlrd.open_workbook("C:\\Users\\Arumugam\\PycharmProjects\\ECommerce_Demo\\TestData\\InputData.xlsx")
sheet = workbook.sheet_by_name("discount")

# Get no of rows and columns
rowsCount = sheet.nrows
colsCount = sheet.ncols

print("Rows->", rowsCount)
print("Columns", colsCount)

for r in range(1, rowsCount):
    discount_name = sheet.cell_value(r, 0)
    discount_type = sheet.cell_value(r, 1)
    discount_amt = sheet.cell_value(r, 2)
    start_date = sheet.cell_value(r, 3)
    end_date = sheet.cell_value(r, 4)
    discount_limit = sheet.cell_value(r, 5)
    search_discount_type = sheet.cell_value(r, 6)
    search_discount_name = sheet.cell_value(r, 7)

    print('Enter user details')

    self.lp = LoginPage(self.driver)
    print('Enter user name')
    self.lp.setUserName(self.username)
    print('Enter password')
    self.lp.setPassword(self.password)
    print('click login btn')
    self.lp.clickLogin()
    self.logger.info("***********Login Successful*************")
    self.discount = AddDiscount(self.driver)
    print('click promo link')
    self.discount.clickPromotionLink()
    print('click discount link')
    self.discount.clickDiscountLink()
    print('click add new btn')
    self.discount.clickAddNew()
    print('enter discount name')
    self.discount.enterDiscountName(discount_name)
    self.discount.selectDiscountType(discount_type)
    self.discount.enterDiscountAmount(discount_amt)
    self.discount.enterStartDate(start_date)
    self.discount.enterEndDate(end_date)
    self.discount.selectDiscountLimit(discount_limit)
    time.sleep(5)
    self.discount.clickSaveBtn()
    self.logger.info("Discount details entered successfully")
    self.logger.info("Search Discount details and edit information")
    self.discount.searchDiscountType(search_discount_type)
    #self.discount.enterSearchDiscountName(search_discount_name)
    self.discount.clickSearchBtn()
    self.discount.verifyDiscountTypeText(search_discount_type)
    self.discount.clickLogOutBtn()

