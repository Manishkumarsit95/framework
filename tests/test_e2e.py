import time

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
#@pytest.mark.usefixtures("setup") - We have created base class to remove fixture redundent
from PageObject.CheckoutPage import CheckOutPage
from PageObject.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):
    def test_e2e(self):
        log = self.getlogger()
        homePage = HomePage(self.driver)
        homePage.shopItems().click()
        # Xpath - //a[text()='Shop'] , 2nd xpath - //a[contains(@href,'shop')] CSS- Selector- a[href='/angularpractice/shop']
        # Css - a[href*='shop']
        #Self . driver because whe we inheritance the class variable then use self.
        #self.driver.find_element(By.CSS_SELECTOR, "a[href='/angularpractice/shop']").click()
        # Xpath for all the product list - //div[@class='card h-100']
        checkOutPage = CheckOutPage(self.driver)
        log.info("getting all the card title")
        Products = checkOutPage.getcartTitle()
        #Products = self.driver.find_elements(By.XPATH, "//div[@class='card h-100']")
        for product in Products:
            productName = product.find_element(By.XPATH, "div/h4/a").text
            log.info(productName)
            if productName == "Blackberry":
                product.find_element(By.XPATH, "div/button").click()
        self.driver.find_element(By.CSS_SELECTOR, "a[class*='nav-link btn btn-primary']").click()
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
        log.info("Entering Country Name as Ind")
        self.driver.find_element(By.ID, "country").send_keys("Ind")
        #wait = WebDriverWait(self.driver, 20)
        #wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
        self.verifyLinkPresence("India")
        self.driver.find_element(By.LINK_TEXT, "India").click()
        self.driver.find_element(By.XPATH, "//label[@for='checkbox2']").click()
        self.driver.find_element(By.XPATH, "//input[@class='btn btn-success btn-lg']").click()
        SuccessText = self.driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissible']").text
        log.info("Text recieved from application is "+SuccessText)
        assert "Success! Thank you!" in SuccessText


