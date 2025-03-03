import pytest
from selenium.webdriver.common.by import By

def test_dashItems_Recr(driver_Inst):
    assert driver_Inst.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[5]/a/span').text == "Recruitment"

def test_dashItems_MyInfo(driver_Inst):
    assert driver_Inst.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[6]/a/span').text == "My Info"

def test_dashItems_Direct(driver_Inst):
    assert driver_Inst.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[9]/a/span').text == "Directory"