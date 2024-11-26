import pytest
from selenium.webdriver.common.by import By

def test_dashItems_main(driver_Inst):
    assert driver_Inst.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[10]/a/span').text == "Maintenance"

def test_dashItems_claim(driver_Inst):
    assert driver_Inst.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[11]/a/span').text == "Claim"  