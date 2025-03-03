import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

@pytest.fixture(scope="package")
def driver_Inst():
    serviceObject = Service(executable_path="./drivers/chromedriver.exe")
    driver = webdriver.Chrome(service=serviceObject)
    driver.implicitly_wait(10)
    driver.get(url="https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(10)
    yield driver
    driver.close()
