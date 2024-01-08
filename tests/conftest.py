import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome" )


@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("--browser_name")
    if browser_name == "chrome":
        service_obj = Service("C:\\Users\\manish.kumar20\\Documents\\chromedriver_win32\\chromedriver.exe")
        driver = webdriver.Chrome(service=service_obj)
    elif browser_name == "IE":
        service_obj = Service("C:\\Users\\manish.kumar20\\Documents\\edgedriver_win64\\msedgedriver.exe")
        driver = webdriver.Edge(service=service_obj)
    elif browser_name == "firefox":
        print("firefox")
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()