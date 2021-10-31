import time

from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.select import Select


class AddCustomerRole:
    link_cust_role_xpath = "//p[contains(text(),'Customer roles')]"
    link_addNew_xpath = "//a[@class='btn btn-primary']"
    link_customer_name_xpath = "//input[@id='Name']"
    chkBox_cust_active_chk_box = "//input[@id='Active']"
    chkBox_cust_freeship_css = "#FreeShipping"
    chkBox_cust_tax_xpath = "//input[@id='TaxExempt']"
    chkBox_cust_tax_display_type_css = "#OverrideTaxDisplayType"
    chkBox_cust_enable_password_lifeTime_xpath = "//input[@id='EnablePasswordLifetime']"
    btn_cust_purchase_prod_xpath = "//button[normalize-space()='Choose a product']"
    btn_select_product_xpath = "//tbody/tr[1]/td[1]/button[1]"
    btn_select_show_xpath = "//select[@name='products-grid_length']"
    btn_refresh_css = ".fas.fa-sync-alt"
    btn_save_xpath = "//button[@name='save']"
    txt_prod_name_css = "#SearchProductName"
    btn_search_xpath = "//button[@id='search-products']"
    btn_edit_xpath = "(//a[@class='btn btn-default'])[4]"
    links_edit_menu_xpath = "//*[@id='customerroles-grid']/tbody/tr"
    btn_delete_xpath = "//span[@id='customerrole-delete']"
    btn_delete_confirm_xpath = "//button[@class='btn btn-danger float-right']"

    def __init__(self, driver):
        self.driver = driver

    def clickCustomerRole(self):
        self.driver.find_element_by_xpath(self.link_cust_role_xpath).click()

    def clickAddNewBtn(self):
        self.driver.find_element_by_xpath(self.link_addNew_xpath).click()

    def enterCustomerName(self, custname):
        self.driver.find_element_by_xpath(self.link_customer_name_xpath).send_keys(custname)

    def clickCustomerActiveChkBox(self):
        checkbox = self.driver.find_element_by_xpath(self.chkBox_cust_active_chk_box);
        if checkbox.is_selected:
            print("Checkbox Active is already selected")
        else:
            self.driver.find_element_by_xpath(self.chkBox_cust_active_chk_box).click()

    def clickCustomerFreeShipChkBox(self):
        try:
            self.driver.find_element_by_css_selector(self.chkBox_cust_freeship_css).click()
            print('freeship chk box clicked')
        except StaleElementReferenceException:
            self.driver.find_element_by_css_selector(self.chkBox_cust_freeship_css).click()

    def clickCustomerTaxChkBox(self):
        self.driver.find_element_by_xpath(self.chkBox_cust_tax_xpath).click()

    def clickCustomerTaxDisplayChkBox(self):
        self.driver.find_element_by_css_selector(self.chkBox_cust_tax_display_type_css).click()

    def clickCustomerEnablePass(self):
        self.driver.find_element_by_xpath(self.chkBox_cust_enable_password_lifeTime_xpath).click()

    def clickCustomerPurchaseBtn(self):
        self.main_page = self.driver.current_window_handle
        print("MainPage->", self.main_page)
        print("Current Page ->", self.driver.title)
        time.sleep(5)
        self.driver.find_element_by_xpath(self.btn_cust_purchase_prod_xpath).click()
        print("changing the handles to access popup page")
        for handle in self.driver.window_handles:
            if handle != self.main_page:
                product_page = handle

        # change the control to choose product page
        self.driver.switch_to.window(product_page)

        print("Scroll Down to the page")
        self.driver.execute_script("window.scrollTo(0, 1000);")
        time.sleep(3)

        print("select dropdown for count")
        self.driver.find_element_by_xpath(self.btn_select_show_xpath).click()
        time.sleep(3)
        element = self.driver.find_element_by_xpath(self.btn_select_show_xpath)
        drop = Select(element)
        # drop.select_by_index(2)
        time.sleep(3)
        drop.select_by_visible_text('20')
        print("dropdown selected for count values")
        self.driver.execute_script("window.scrollTo(0, -1000);")
        print("scrolled up successfully")
        self.driver.find_element_by_css_selector(self.txt_prod_name_css).click()
        self.driver.find_element_by_css_selector(self.txt_prod_name_css).send_keys('Apple')
        time.sleep(2)
        self.driver.find_element_by_xpath(self.btn_search_xpath).click()
        print("search btn clicked successfully")
        time.sleep(3)
        self.driver.find_element_by_xpath(self.btn_select_product_xpath).click()
        print("product selected successfully")
        print("switch to default window")
        self.driver.switch_to.window(self.main_page)
        print(self.driver.title)

    def chooseProductName(self):
        print("Scroll Down to the page")
        self.driver.execute_script("window.scrollTo(0, 1000);")
        time.sleep(3)

    def selectShowDropdown(self):
        print("select dropdown for count")
        self.driver.find_element_by_xpath(self.btn_select_show_xpath).click()
        time.sleep(3)
        element = self.driver.find_element_by_xpath(self.btn_select_show_xpath)
        drop = Select(element)
        # drop.select_by_index(2)
        time.sleep(3)
        drop.select_by_visible_text('20')
        print("dropdown selected for count values")
        self.driver.execute_script("window.scrollTo(0, -1000);")
        print("scrolled up successfully")
        self.driver.find_element_by_css_selector(self.txt_prod_name_css).click()
        self.driver.find_element_by_css_selector(self.txt_prod_name_css).send_keys('Apple')
        time.sleep(2)
        self.driver.find_element_by_xpath(self.btn_search_xpath).click()
        print(self.driver.title)
        print("search btn clicked successfully")
        self.driver.find_element_by_xpath(self.btn_select_product_xpath).click()
        print(self.driver.title)
        print("switch to default window")
        # self.driver.switch_to.window(main_page)
        # self.driver.switch_to.default_window()
        print("switched to default window successfully")

    def clickRefreshButton(self):
        self.driver.find_element_by_xpath(self.btn_refresh_css).click()

    def clickSaveButton(self):
        time.sleep(2)
        self.driver.find_element_by_xpath(self.btn_save_xpath).click()
        print("save btn clicked")

    def clickEditButton(self):
        time.sleep(3)
        print('fetch customer role lists')
        print('get customer role links')
        print("click edit btn")
        self.driver.find_element_by_xpath(self.btn_edit_xpath).click()
        print("edit btn clicked successfully")


    def clickDeleteButton(self):
        time.sleep(2)
        self.driver.find_element_by_xpath(self.btn_delete_xpath).click()
        print("delete btn clicked")

    def clickConfirmDeleteButton(self):
        time.sleep(2)
        self.driver.find_element_by_xpath(self.btn_delete_confirm_xpath).click()
        print("delete btn clicked")

    def clickEditBtnInWebTable(self):
        time.sleep(3)
        print('fetch customer role lists')
        table = self.driver.find_element_by_xpath("//table[@id='customerroles-grid']")
        tbody = table.find_element_by_tag_name("tbody")
        rows = tbody.find_elements_by_tag_name("tr")
        print(len(rows))
        cells = tbody.find_elements_by_tag_name("td")

        for i in range(len(rows)):
            columns = rows[i].find_elements_by_tag_name("td")
            for j in range(len(columns)):
                if columns[j].text == "Administrators":
                    print('Verify the role name and click edit')
                    columns[5].click()
                    print('Admin role clicked')
        time.sleep(3)
        print('Click freeshiping check box')

