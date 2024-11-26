import pytest
from selenium.webdriver.common.by import By

def test_dashItems_dash(driver_Inst):
    assert driver_Inst.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[8]/a/span').text == "Dashboard"

def test_dashItems_perf(driver_Inst):
    assert driver_Inst.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[7]/a/span').text == "Performance"