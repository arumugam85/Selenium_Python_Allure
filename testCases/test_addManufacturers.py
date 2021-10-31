import self
import xlrd
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from pageObjects.AddManufacturers import AddManufacturers
from pageObjects.AddProducts import AddProducts
from pageObjects.LoginPage import LoginPage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig

## Read data from config files
self.baseURL = ReadConfig.getApplicationURL()
self.username = ReadConfig.getUsername()
self.password = ReadConfig.getPassword()
self.logger = LogGen.loggen()

self.driver = webdriver.Chrome(ChromeDriverManager().install())
self.driver.implicitly_wait(10)

print('Launch Nop commerce application')
# self.driver.get("https://admin-demo.nopcommerce.com/Admin")
self.driver.get(self.baseURL)
self.driver.maximize_window()

## Create Workbook sheet
path = ".//TestData/InputData.xlsx"
workbook = xlrd.open_workbook("C:\\Users\\Arumugam\\PycharmProjects\\ECommerce_Demo\\TestData\\InputData.xlsx")
sheet = workbook.sheet_by_name("manufacturer")

# Get no of rows and columns
rowsCount = sheet.nrows
colsCount = sheet.ncols

print("Rows->", rowsCount)
print("Columns", colsCount)

for r in range(1, rowsCount):
    mfg_name = sheet.cell_value(r, 0)
    mfg_desc = sheet.cell_value(r, 1)
    map_discount_name = sheet.cell_value(r, 2)
    limit_cust_role = sheet.cell_value(r, 3)
    limit_store_name = sheet.cell_value(r, 4)

    print('Enter user details')
    self.lp = LoginPage(self.driver)
    print('Enter user name')
    self.lp.setUserName(self.username)
    print('Enter password')
    self.lp.setPassword(self.password)
    print('click login btn')
    self.lp.clickLogin()
    self.logger.info("***********Login Successful*************")
    self.manufacture = AddManufacturers(self.driver)
    print('click promo link')
    self.products = AddProducts(self.driver)
    self.products.clickCategoryLink()
    self.manufacture.clickManufactureLink()
    self.products.clickAddNewBtn()
    print('click toggle btn')
    # self.manufacture.clickToggleBtn()
    self.manufacture.enterMfgDiscountName(mfg_name)
    self.manufacture.enterDiscountDesc(mfg_desc)
    self.manufacture.clickUploadBtn()
    self.manufacture.clickMappingsBtn()
    self.manufacture.selectLimitStoreType(limit_store_name)
    self.manufacture.selectLimitRoleType(limit_cust_role)
    self.products.clickSaveBtn()
    self.manufacture.clickChkBoxTable()
    self.manufacture.clickDeleteBtn()
    self.manufacture.exportExcelFile()
    self.manufacture.importExcelFile()
    self.logger.info("manufacturer details excel file imported successfully")

    self.msg = self.driver.find_element_by_xpath("//div[@class='alert alert-success alert-dismissable']").text
    print("Success Msg->", self.msg)

    if 'Manufacturers have been imported successfully.' in self.msg:
        assert True == True
        print('test passed')
        self.logger.info("**** Add Manufacturer details test case is passed  ****")

    else:
        assert True == False
        self.logger.info("**** Add Manufacturer details  test case is failed  ****")

