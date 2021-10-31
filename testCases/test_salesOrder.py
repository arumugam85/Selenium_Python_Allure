import json
import allure
import logging

from pageObjects.AddProducts import AddProducts
from pageObjects.LoginPage import LoginPage
from pageObjects.SalesPage import SalesPage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class Test_001_SalesOrder:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    # Create and configure logger
    logging.basicConfig(filename="test.log",
                        format='%(asctime)s %(message)s',
                        filemode='w')

    # Creating an object
    logger = logging.getLogger()

    # Setting the threshold of logger to DEBUG
    logger.setLevel(logging.DEBUG)

    def test_read_excel_column_file(self):
        logging.debug('This is a debug message')
        logging.info('This is an info message')
        logging.warning('This is a warning message')
        logging.error('This is an error message')
        logging.critical('This is a critical message')

    @allure.description("**********Validate NOP commerce application with login credentials**********")
    @allure.severity(severity_level="CRITICAL")
    def test_login(self, setup):
        self.logger.info("****Started Login Test****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.products = AddProducts(self.driver)
        self.products.clickCategoryLink()
        self.sales = SalesPage(self.driver)
        self.sales.clickSalesLink()
        self.sales.clickOrdersLink()
        self.sales.verifyOrdersWebTable()
        self.sales.clickPrintPdfVoices()
        self.sales.clickOrdersLink()
        self.sales.verifyBillingCountryType()
        self.sales.rightClickPdfVoices()

    @allure.description("**********Validate NOP commerce application for GiftCard information**********")
    @allure.severity(severity_level="CRITICAL")
    def test_enterGiftCardDetails(self, setup):
        print('Read Json file')
        with open("C:/Users/Arumugam/PycharmProjects/ECommerce_Demo/TestData/test_giftCardData.json",
                  encoding='utf-8') as gift:
            data = json.loads(gift.read())
        print(data)

        self.logger.info("****Started Login Test****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.products = AddProducts(self.driver)
        self.products.clickCategoryLink()
        self.sales = SalesPage(self.driver)
        self.sales.clickSalesLink()
        print('Enter gift card details')
        self.sales.clickGiftCardLink()
        self.sales.clickAddNewBtn()
        self.sales.selectCardType(data["cardInfo"]["cardType"])
        self.sales.clickGenerateCodeBtn()
        self.sales.enterInitialValue(data["cardInfo"]["initValue"])
        self.sales.enterRecipientName(data["cardInfo"]["recipName"])
        # self.sales.enterRecipEmail(data["cardInfo"]["recipEmail"])
        self.sales.enterSenderName(data["cardInfo"]["senderName"])
        # self.sales.enterSenderEmail(data["cardInfo"]["senderEmail"])
        self.sales.enterMessage(data["cardInfo"]["message"])
        self.sales.clickSaveBtn()

        actualMsg = self.driver.find_element_by_xpath("//div[@class='alert alert-success alert-dismissable']")
        print(actualMsg.text)
        self.driver.quit()
