import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class SalesPage:
    link_sales_xpath = "//p[normalize-space()='Sales']"
    link_orders_xpath = "//p[normalize-space()='Orders']"
    btn_pdf_voice_xpath = "//button[@class='btn btn-info dropdown-toggle dropdown-icon']"
    btn_selected_pdf_invoice_xpath = "//button[@id='pdf-invoice-selected']"
    txt_manufacture_name_xpath = "//input[@id='Name']"
    drp_limit_role_xpath = "(//div[@class='k-multiselect-wrap k-floatwrap'])[2]"
    drp_limit_store_xpath = "(//div[@class='k-multiselect-wrap k-floatwrap'])[3]"
    btn_manufacture_mappings_xpath = "//div[@id='manufacturer-mappings']"
    menu_custrole_xpath = "//li[contains(text(),'Administrators')]"
    menu_limitstore_xpath = "//li[contains(text(),'Test store 2')]"
    txt_manufacture_desc_id = "Description_ifr"
    btn_upload_xpath = "//div[@class='upload-image-button float-left px-md-1']"
    btn_save_xpath = "//button[@name='save']"
    link_insert_xpath = "//span[normalize-space()='Insert']"
    select_datetime_menu_xpath = "//div[contains(text(),'Date/time')]"
    link_datetime_date_xpath = "div[title='2021-10-24'] div[class='tox-collection__item-label']"
    btn_search_xpath = "//button[@id='search-discounts']"
    btn_logout_xpath = "//a[normalize-space()='Logout']"
    txt_discount_type_css = "tr[class='odd'] td:nth-child(2)"
    txt_mfg_discount_name_xpath = "//input[@id='Name']"
    btn_delete_selected_id = "delete-selected"
    btn_delete_confirm_id = "delete-selected-action-confirmation-submit-button"
    ##Gift cards page
    btn_addNew_xpath = "//a[@class='btn btn-primary']"
    link_gift_cards_xpath = "//p[normalize-space()='Gift cards']"
    btn_card_type_xpath = "//select[@id='GiftCardTypeId']"
    txt_initial_value_xpath = "//input[@class='k-formatted-value k-input']"
    btn_gen_coupon_xpath = "//button[@id='generateCouponCode']"
    txt_recip_name_xpath = "//input[@id='RecipientName']"
    txt_recip_email_xpath = "//input[@id='RecipientEmail']"
    txt_sender_name_xpath = "//input[@id='SenderName']"
    txt_sender_email_xpath = "//input[@id='SenderEmail']"
    txt_message_css = "#Message"

    def __init__(self, driver):
        self.driver = driver

    def clickSalesLink(self):
        try:
            self.driver.find_element_by_xpath(self.link_sales_xpath).click()

        except Exception as e:
            print("Manufacture link is not clickable")

    def clickOrdersLink(self):
        try:
            self.driver.find_element_by_xpath(self.link_orders_xpath).click()
        except Exception as e:
            print("Element is not clickable")

    def verifyOrdersWebTable(self):
        print("fetch all the rows from web tables")
        self.driver.execute_script("window.scrollTo(0, 500);")
        table = self.driver.find_element_by_xpath("//*[@id='orders-grid']")
        tbody = table.find_element_by_tag_name("tbody")
        rows = tbody.find_elements_by_tag_name("tr")
        print(len(rows))
        cells = tbody.find_elements_by_tag_name("td")

        print("verify tables")
        for i in range(len(rows)):
            columns = rows[i].find_elements_by_tag_name("td")
            for j in range(len(columns)):
                if columns[j].text == "Paid":
                    print('Verify the payment status click check box')
                    columns[0].click()
                    print('chk box clicked for rows:', i)
                    time.sleep(3)

    def clickPrintPdfVoices(self):
        self.driver.execute_script("window.scrollTo(0, -1000);")
        try:
            self.driver.find_element_by_xpath(self.btn_pdf_voice_xpath).click()
            time.sleep(2)
            self.driver.find_element_by_xpath(self.btn_selected_pdf_invoice_xpath).click()
            time.sleep(3)
        except Exception as e:
            print("Element is not clickable")

    def rightClickPdfVoices(self):
        print("right click pdf button")
        try:
            actions = ActionChains(self.driver)
            pdf_button = self.driver.find_element_by_xpath(self.btn_pdf_voice_xpath)
            actions.context_click(pdf_button).perform()
            time.sleep(2)

        except Exception as e:
            print("Element is not clickable")

    def verifyBillingCountryType(self):
        self.driver.refresh()
        time.sleep(5)
        print("select billing country from the list")

        try:
            countryDD = self.driver.find_element_by_xpath("//*[@id='BillingCountryId']")
            country = Select(countryDD)
            country_list = country.options
            print('No of countries', len(country_list))
            time.sleep(3)

            for country in country_list:
                print('Countries list:', country.text)
                if country.text == "India":
                    country.click()
                    break

        except Exception as e:
            print("dropdown value is not clickable")

    def enterDiscountDesc(self, mfg_desc):
        self.driver.find_element_by_id(self.txt_manufacture_desc_id).send_keys(mfg_desc)

    def selectLimitRoleType(self, limit_cust_role):
        time.sleep(10)
        print("select limit_cust_role menu from list")

        try:
            self.driver.find_element_by_xpath("(//div[@class='k-multiselect-wrap k-floatwrap'])[2]").click()
            time.sleep(3)
            self.driver.find_element_by_xpath("//li[contains(text(),'Administrators')]").click()
            print("select multi dropdown from list")
            time.sleep(3)
            self.driver.find_element_by_xpath("//li[contains(text(),'Guests')]").click()
            time.sleep(3)
            self.driver.find_element_by_xpath("//li[contains(text(),'Vendors')]").click()
            print("dropdown value selected successfully")
            print("Scroll Down to the page")
            self.driver.execute_script("window.scrollTo(0, -1000);")
            time.sleep(3)
        except Exception as e:
            print("dropdown value is not clickable")

    def selectLimitStoreType(self, limitstore_type):
        time.sleep(3)
        print("select limit store dropdown")

        try:
            self.driver.find_element_by_xpath("(//div[@class='k-multiselect-wrap k-floatwrap'])[3]").click()
            time.sleep(3)
            self.driver.find_element_by_xpath("//li[contains(text(),'Test store 2')]").click()
            # select.select_by_visible_text("Computers")
            print("dropdown value selected successfully")
        except Exception as e:
            print("dropdown value is not clickable")

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
        self.driver.find_element_by_xpath(self.btn_save_xpath).click()
        # wait = WebDriverWait(self.driver, 10)
        # wait.until(EC.element_to_be_clickable(By.XPATH, "//button[@name='save']")).click()
        print('clicked save btn')

    def searchMfgLimitRoleType(self, search_discount_type):
        time.sleep(3)
        print("select discount type")
        dropdown1 = Select(self.driver.find_element_by_xpath(self.select_discount_type_xpath))
        dropdown1.select_by_visible_text(search_discount_type)

    def enterMfgDiscountName(self, mfg_name):
        self.driver.find_element_by_xpath(self.txt_mfg_discount_name_xpath).click()
        self.driver.find_element_by_xpath(self.txt_mfg_discount_name_xpath).send_keys(mfg_name)

    def clickMappingsBtn(self):
        time.sleep(3)
        self.driver.execute_script("window.scrollTo(0, 1000);")
        time.sleep(2)
        self.driver.find_element_by_xpath(self.btn_manufacture_mappings_xpath).click()

    def clickToggleBtn(self):
        time.sleep(2)
        self.driver.find_element_by_xpath(self.btn_toggle_xpath).click()

    def clickUploadBtn(self):
        time.sleep(5)
        print('verify image upload btn')
        element = self.driver.find_element_by_xpath(self.btn_upload_xpath)
        if element.is_displayed():
            print('upload images btn is displayed already')

        else:
            self.driver.find_element_by_xpath(self.btn_toggle_xpath).click()
            print('toggle btn is clicked')
        print('upload images')
        self.driver.find_element_by_xpath("//input[@title='file input']").send_keys(
            "C:/Users/Arumugam/images/google.jpg")

    def verifyDiscountTypeText(self, search_discount_type):
        time.sleep(3)
        discount_type = self.driver.find_element_by_css_selector(self.txt_discount_type_css)
        print("Actual Text ->", discount_type.text)
        print("Expected Text ->", search_discount_type)

        if discount_type.text == search_discount_type:
            # self.logger.info("**** Search discount type passed ****")
            print('Text matches passed')
            # self.driver.close()
            assert True
        else:
            # self.logger.error("**** Search discount type failed ****")
            print('Text matches Failed')
            self.driver.save_screenshot(".\\Screenshots\\" + "test_disocuntType.png")
            # self.driver.close()
            assert False

    def importExcelFile(self):
        time.sleep(5)
        print('verify import btn')
        print('import excel')
        self.driver.find_element_by_xpath("//button[@name='importexcel']").click()
        print('choose excel file')
        self.driver.find_element_by_xpath("//input[@id='importexcelfile']").send_keys(
            "C:/Users/Arumugam/images/manufacturers.xlsx")
        self.driver.find_element_by_xpath("//button[normalize-space()='Import from Excel']").click()
        print('excel file imported sucessfully')

    def exportExcelFile(self):
        time.sleep(5)
        print('verify export btn')
        print('export excel file')
        self.driver.find_element_by_xpath("//button[@class='btn btn-success dropdown-toggle']").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("(//li[@class='dropdown-item'])[3]").click()
        print('excel file export successfully')

    def clickChkBoxTable(self):
        time.sleep(3)
        self.driver.find_element_by_xpath("//tbody/tr[1]/td[1]").click()

    def clickDeleteBtn(self):
        time.sleep(4)
        self.driver.find_element_by_id(self.btn_delete_selected_id).click()
        time.sleep(2)
        self.driver.find_element_by_id(self.btn_delete_confirm_id).click()

    def clickGiftCardLink(self):
        try:
            self.driver.find_element_by_xpath(self.link_gift_cards_xpath).click()
        except Exception as e:
            print("Element is not clickable")

    def clickAddNewBtn(self):
        time.sleep(3)
        self.driver.find_element_by_xpath(self.btn_addNew_xpath).click()

    def selectCardType(self, cardType):
        time.sleep(3)
        print("enter card type")
        selectDiscount = Select(self.driver.find_element_by_xpath(self.btn_card_type_xpath))
        selectDiscount.select_by_visible_text(cardType)

    def enterRecipientName(self, recipName):
        self.driver.find_element_by_xpath(self.txt_recip_name_xpath).click()
        self.driver.find_element_by_xpath(self.txt_recip_name_xpath).send_keys(recipName)

    def enterInitialValue(self, initValue):
        self.driver.find_element_by_xpath(self.txt_initial_value_xpath).click()
        self.driver.find_element_by_xpath("//input[@id='Amount']").send_keys(initValue)

    def enterRecipEmail(self, recipEmail):
        self.driver.find_element_by_xpath(self.txt_recip_email_xpath).click()
        self.driver.find_element_by_xpath(self.txt_recip_email_xpath).send_keys(recipEmail)

    def enterSenderName(self, senderName):
        self.driver.find_element_by_xpath(self.txt_sender_name_xpath).click()
        self.driver.find_element_by_xpath(self.txt_sender_name_xpath).send_keys(senderName)

    def enterSenderEmail(self, senderEmail):
        self.driver.find_element_by_xpath(self.txt_sender_email_xpath).click()
        self.driver.find_element_by_xpath(self.txt_sender_email_xpath).send_keys(senderEmail)

    def enterMessage(self, message):
        self.driver.find_element_by_css_selector(self.txt_message_css).send_keys(message)

    def clickGenerateCodeBtn(self):
        time.sleep(3)
        self.driver.find_element_by_xpath(self.btn_gen_coupon_xpath).click()
