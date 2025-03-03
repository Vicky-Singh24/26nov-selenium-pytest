import pytest
from selenium.webdriver.common.by import By

def test_dashItems_Admin(driver_Inst):
    assert driver_Inst.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a/span').text == "Admin"

def test_dashItems_PIM(driver_Inst):
    assert driver_Inst.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a/span').text == "PIM"

def test_dashItems_Leave(driver_Inst):
    assert driver_Inst.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[3]/a/span').text == "Leave"

def test_dashItems_Time(driver_Inst):
    assert driver_Inst.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[4]/a/span').text == "Time"