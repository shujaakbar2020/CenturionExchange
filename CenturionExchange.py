import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Centurion(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def create_quick_inventory(self):
        driver = self.driver
        driver.get("https://www.centurionexchange.com/ui/createQuickInventory.xhtml")
        driver.find_element_by_id("UserName").send_keys("helpadmin@centurionexchange.com")
        driver.find_element_by_id("passwordTxtId").send_keys("Test123!")
        driver.find_element_by_id("loginBtnId").click()
        driver.find_element_by_id("menuForm:j_idt35:3:j_idt37:4:j_idt38").click()

        driver.find_element_by_id("userAccountId_label").click()
        content = driver.find_element_by_xpath("//*[@id='userAccountId_panel']/div[2]/ul")
        items = content.find_elements_by_tag_name('li')
        for item in items:
            if item.text == "Centurion Service":
                item.click()

        driver.implicitly_wait(10)

        driver.find_element_by_xpath("//*[@id='inventoryDetailTable_data']/tr/td[1]/div/div[2]").click()

        driver.find_element_by_xpath("//*[@id='inventoryDetailTable:0:manufacturerID']/input").send_keys("DevHood")
        driver.implicitly_wait(5)
        driver.find_element_by_xpath("//*[@id='inventoryDetailTable:0:modelID']/input").send_keys("3221")
        driver.implicitly_wait(5)
        driver.find_element_by_xpath("//*[@id='inventoryDetailTable:0:itemID']/input").send_keys("Glass")
        driver.implicitly_wait(5)
        driver.find_element_by_xpath("//*[@id='inventoryDetailTable:0:categoryID_input']").send_keys("Glass")
        driver.find_element_by_xpath("//*[@id='inventoryDetailTable:0:itemDesc']").send_keys("This is new Glass")

        # driver.find_element_by_id("inventoryDetailTable:0:status_label").click()
        content1 = driver.find_element_by_xpath("//*[@id='inventoryDetailTable:0:status_panel']/div/ul")
        items1 = content1.find_elements_by_tag_name('li')
        for item1 in items1:
            if item1.text == "FOR SALE":
                item1.click()

        driver.implicitly_wait(10)

        condition = driver.find_element_by_xpath("//*[@id='inventoryDetailTable:0:condition_panel']/div/ul")
        items2 = condition.find_elements_by_tag_name('li')
        for item in items2:
            if item.text == "New":
                item.click()

        driver.find_element_by_xpath("//*[@id='inventoryDetailTable:0:manu7']").send_keys("112211")
        driver.find_element_by_xpath("//*[@id='inventoryDetailTable:0:manu8']").send_keys("12321")
        driver.find_element_by_xpath("//*[@id='inventoryDetailTable:0:manu9']").send_keys("222")
        driver.find_element_by_xpath("//*[@id='inventoryDetailTable:0:manu11']").send_keys("First One")
        driver.find_element_by_xpath("//*[@id='inventoryDetailTable:0:manu11']").send_keys("12")
        driver.find_element_by_xpath("//*[@id='inventoryDetailTable:0:j_idt127']").send_keys("This is rare item")
        driver.find_element_by_xpath("//*[@id='inventoryDetailTable:0:fairMarketValue_input']").send_keys("110")
        driver.find_element_by_xpath("//*[@id='inventoryDetailTable:0:netBookValue_input']").send_keys("110")
        driver.find_element_by_xpath("//*[@id='inventoryDetailTable:0:cost_input']").send_keys("110")
        driver.find_element_by_xpath("//*[@id='inventoryDetailTable:0:boxQuantity']").send_keys("2")
        driver.find_element_by_xpath("//*[@id='inventoryDetailTable:0:caseQuantity']").send_keys("10")
        driver.find_element_by_xpath("//*[@id='inventoryDetailTable:0:expirationDate_input']").send_keys("01/06/2020")
        driver.implicitly_wait(10)
        driver.find_element_by_xpath("//*[@id='j_idt144']/span").click()
        # driver.find_element_by_id("j_idt144").click()
        assert "Inventory is saved successfully" in driver.page_source

    def search_inventory(self):
        driver = self.driver
        driver.get("https://www.centurionexchange.com/ui/createQuickInventory.xhtml")
        driver.find_element_by_id("UserName").send_keys("helpadmin@centurionexchange.com")
        driver.find_element_by_id("passwordTxtId").send_keys("Test123!")
        driver.find_element_by_id("loginBtnId").click()
        driver.find_element_by_id("menuForm:j_idt35:4:j_idt37:1:j_idt38").click()
        driver.find_element_by_id("wildCardSearch").send_keys("Glass")
        driver.find_element_by_id("wildCardSearch").send_keys(Keys.ENTER)
        driver.implicitly_wait(10)
        content = driver.find_element_by_xpath("//*[@id='inventoryDetailGrid:0:j_idt107']/div[1]/span[1]")
        # self.assertFalse(content.text == "DevHood")
        # self.assertEqual(content.text, "DevHood \n3223")
        assert "DevHood" in content.text

    def create_new_inventory_with_present_inventory_credentials(self):
        driver = self.driver
        driver.get("https://www.centurionexchange.com/ui/createQuickInventory.xhtml")
        driver.find_element_by_id("UserName").send_keys("helpadmin@centurionexchange.com")
        driver.find_element_by_id("passwordTxtId").send_keys("Test123!")
        driver.find_element_by_id("loginBtnId").click()
        driver.find_element_by_id("menuForm:j_idt35:3:j_idt37:4:j_idt38").click()

        driver.find_element_by_id("userAccountId_label").click()
        content = driver.find_element_by_xpath("//*[@id='userAccountId_panel']/div[2]/ul")
        items = content.find_elements_by_tag_name('li')
        for item in items:
            if item.text == "Centurion Service":
                item.click()

        driver.implicitly_wait(10)

        driver.find_element_by_xpath("//*[@id='inventoryDetailTable_data']/tr/td[1]/div/div[2]").click()

        driver.find_element_by_xpath("//*[@id='inventoryDetailTable:0:manufacturerID']/input").send_keys("DevHood")
        driver.implicitly_wait(5)
        driver.find_element_by_xpath("//*[@id='inventoryDetailTable:0:modelID']/input").send_keys("3221")
        driver.implicitly_wait(5)
        driver.find_element_by_xpath("//*[@id='inventoryDetailTable:0:itemID']/input").send_keys("Glass")
        driver.implicitly_wait(5)
        driver.find_element_by_xpath("//*[@id='inventoryDetailTable:0:categoryID_input']").send_keys("Glass")
        driver.find_element_by_xpath("//*[@id='inventoryDetailTable:0:itemDesc']").send_keys("This is new Glass")

        # driver.find_element_by_id("inventoryDetailTable:0:status_label").click()
        content1 = driver.find_element_by_xpath("//*[@id='inventoryDetailTable:0:status_panel']/div/ul")
        items1 = content1.find_elements_by_tag_name('li')
        for item1 in items1:
            if item1.text == "FOR SALE":
                item1.click()

        driver.implicitly_wait(10)

        condition = driver.find_element_by_xpath("//*[@id='inventoryDetailTable:0:condition_panel']/div/ul")
        items2 = condition.find_elements_by_tag_name('li')
        for item in items2:
            if item.text == "New":
                item.click()

        driver.find_element_by_xpath("//*[@id='inventoryDetailTable:0:manu7']").send_keys("112211")
        driver.find_element_by_xpath("//*[@id='inventoryDetailTable:0:manu8']").send_keys("12321")
        driver.find_element_by_xpath("//*[@id='inventoryDetailTable:0:manu9']").send_keys("222")
        driver.find_element_by_xpath("//*[@id='inventoryDetailTable:0:manu11']").send_keys("First One")
        driver.find_element_by_xpath("//*[@id='inventoryDetailTable:0:manu11']").send_keys("12")
        driver.find_element_by_xpath("//*[@id='inventoryDetailTable:0:j_idt127']").send_keys("This is rare item")
        driver.find_element_by_xpath("//*[@id='inventoryDetailTable:0:fairMarketValue_input']").send_keys("110")
        driver.find_element_by_xpath("//*[@id='inventoryDetailTable:0:netBookValue_input']").send_keys("110")
        driver.find_element_by_xpath("//*[@id='inventoryDetailTable:0:cost_input']").send_keys("110")
        driver.find_element_by_xpath("//*[@id='inventoryDetailTable:0:boxQuantity']").send_keys("2")
        driver.find_element_by_xpath("//*[@id='inventoryDetailTable:0:caseQuantity']").send_keys("10")
        driver.find_element_by_xpath("//*[@id='inventoryDetailTable:0:expirationDate_input']").send_keys("01/06/2020")
        driver.implicitly_wait(10)
        driver.find_element_by_xpath("//*[@id='j_idt144']/span").click()
        # driver.find_element_by_id("j_idt144").click()
        assert "Inventory is already available" in driver.page_source

    def new_inventory_without_family_permission(self):
        driver = self.driver
        driver.get("https://www.centurionexchange.com/ui/createQuickInventory.xhtml")
        driver.find_element_by_id("UserName").send_keys("helpadmin@centurionexchange.com")
        driver.find_element_by_id("passwordTxtId").send_keys("Test123!")
        driver.find_element_by_id("loginBtnId").click()
        driver.find_element_by_id("menuForm:j_idt35:3:j_idt37:4:j_idt38").click()

        driver.find_element_by_id("userAccountId_label").click()
        content = driver.find_element_by_xpath("//*[@id='userAccountId_panel']/div[2]/ul")
        items = content.find_elements_by_tag_name('li')
        for item in items:
            if item.text == "Centurion Service":
                item.click()

        driver.implicitly_wait(10)

        driver.find_element_by_xpath("//*[@id='inventoryDetailTable_data']/tr/td[1]/div/div[2]").click()

        driver.find_element_by_xpath("//*[@id='inventoryDetailTable:0:manufacturerID']/input").send_keys("DevHood")
        driver.implicitly_wait(5)
        driver.find_element_by_xpath("//*[@id='inventoryDetailTable:0:modelID']/input").send_keys("3221")
        driver.implicitly_wait(5)
        driver.find_element_by_xpath("//*[@id='inventoryDetailTable:0:itemID']/input").send_keys("Glass")
        driver.implicitly_wait(5)
        driver.find_element_by_xpath("//*[@id='inventoryDetailTable:0:categoryID_input']").send_keys("Glass")
        driver.find_element_by_xpath("//*[@id='inventoryDetailTable:0:itemDesc']").send_keys("This is new Glass")

        # driver.find_element_by_id("inventoryDetailTable:0:status_label").click()
        content1 = driver.find_element_by_xpath("//*[@id='inventoryDetailTable:0:status_panel']/div/ul")
        items1 = content1.find_elements_by_tag_name('li')
        for item1 in items1:
            if item1.text == "FOR SALE":
                item1.click()

        driver.implicitly_wait(10)

        condition = driver.find_element_by_xpath("//*[@id='inventoryDetailTable:0:condition_panel']/div/ul")
        items2 = condition.find_elements_by_tag_name('li')
        for item in items2:
            if item.text == "New":
                item.click()

        driver.find_element_by_xpath("//*[@id='inventoryDetailTable:0:manu7']").send_keys("112211")
        driver.find_element_by_xpath("//*[@id='inventoryDetailTable:0:manu8']").send_keys("12321")
        driver.find_element_by_xpath("//*[@id='inventoryDetailTable:0:manu9']").send_keys("222")
        driver.find_element_by_xpath("//*[@id='inventoryDetailTable:0:manu11']").send_keys("First One")
        driver.find_element_by_xpath("//*[@id='inventoryDetailTable:0:manu11']").send_keys("12")
        driver.find_element_by_xpath("//*[@id='inventoryDetailTable:0:j_idt127']").send_keys("This is rare item")
        driver.find_element_by_xpath("//*[@id='inventoryDetailTable:0:fairMarketValue_input']").send_keys("110")
        driver.find_element_by_xpath("//*[@id='inventoryDetailTable:0:netBookValue_input']").send_keys("110")
        driver.find_element_by_xpath("//*[@id='inventoryDetailTable:0:cost_input']").send_keys("110")
        driver.find_element_by_xpath("//*[@id='inventoryDetailTable:0:boxQuantity']").send_keys("2")
        driver.find_element_by_xpath("//*[@id='inventoryDetailTable:0:caseQuantity']").send_keys("10")
        driver.find_element_by_xpath("//*[@id='inventoryDetailTable:0:expirationDate_input']").send_keys("01/06/2020")
        driver.find_element_by_xpath("//*[@id='inventoryDetailTable:0:elegiblePrgSelect']/div[2]").click()
        driver.implicitly_wait(10)
        driver.find_element_by_xpath("//*[@id='j_idt144']/span").click()
        # driver.find_element_by_id("j_idt144").click()
        assert "Inventory is saved successfully" in driver.page_source

    def search_for_without_family_inventory(self):
        driver = self.driver
        driver.get("https://www.centurionexchange.com/ui/createQuickInventory.xhtml")
        driver.find_element_by_id("UserName").send_keys("helpadmin@centurionexchange.com")
        driver.find_element_by_id("passwordTxtId").send_keys("Test123!")
        driver.find_element_by_id("loginBtnId").click()
        driver.find_element_by_id("menuForm:j_idt35:4:j_idt37:1:j_idt38").click()
        driver.find_element_by_id("wildCardSearch").send_keys("Glass")
        driver.find_element_by_id("wildCardSearch").send_keys(Keys.ENTER)
        driver.implicitly_wait(10)
        content = driver.find_element_by_xpath("//*[@id='inventoryDetailGrid:0:j_idt107']/div[1]/span[1]")
        self.assertFalse("DevHood" in content.text)

    def search_inventory_with_filters(self):
        driver = self.driver
        driver.get("https://www.centurionexchange.com/ui/createQuickInventory.xhtml")
        driver.find_element_by_id("UserName").send_keys("helpadmin@centurionexchange.com")
        driver.find_element_by_id("passwordTxtId").send_keys("Test123!")
        driver.find_element_by_id("loginBtnId").click()

        driver.find_element_by_id("manufacturer_label").click()
        content = driver.find_element_by_xpath("//*[@id='manufacturer_panel']/div[2]/ul")
        items = content.find_elements_by_tag_name('li')
        for item in items:
            if item.text == "DevHood":
                item.click()

        driver.find_element_by_id("filterSearchButton").click()
        content = driver.find_element_by_xpath("//*[@id='inventoryDetailGrid:0:j_idt107']/div[1]/span[1]")
        self.assertTrue("DevHood" in content.text)

    def setting_system_config(self):
        driver = self.driver
        driver.get("https://www.centurionexchange.com/ui/createQuickInventory.xhtml")
        driver.find_element_by_id("UserName").send_keys("helpadmin@centurionexchange.com")
        driver.find_element_by_id("passwordTxtId").send_keys("Test123!")
        driver.find_element_by_id("loginBtnId").click()

        driver.find_element_by_xpath("//*[@id='menuForm:j_idt35:2:j_idt37:3:j_idt38']").click()
        driver.find_element_by_id("form:list:4:j_idt69").click()
        driver.find_element_by_id("form:list:4:configValueId").send_keys("testing@gmail.com")
        driver.find_element_by_xpath("//*[@id='form:list:4:j_idt69']/span[2]").click()

        self.assertTrue("updated", "System config updated")

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
