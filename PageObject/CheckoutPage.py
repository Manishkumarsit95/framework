from selenium.webdriver.common.by import By


class CheckOutPage:
    def __init__(self,driver):
        self.driver = driver

    cartTitle = (By.XPATH, "//div[@class='card h-100']")
#Products = self.driver.find_elements(By.XPATH, "//div[@class='card h-100']")
    checkOutClick = (By.CSS_SELECTOR, "a[class*='nav-link btn btn-primary']")
#self.driver.find_element(By.CSS_SELECTOR, "a[class*='nav-link btn btn-primary']").click()

    def getcartTitle(self):
        return self.driver.find_elements(*CheckOutPage.cartTitle)

    def checkOuotClick(self):
        return self.driver.find_elements(*CheckOutPage.checkOutClick)
