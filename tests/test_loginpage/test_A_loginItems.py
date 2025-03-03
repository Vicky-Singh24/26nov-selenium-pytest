import pytest
from selenium.webdriver.common.by import By
import time

def test_logoPresence(driver_Inst):
    assert driver_Inst.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/h5').text == 'Login'

def test_credentialPresence(driver_Inst):
    assert driver_Inst.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/div/div/p[1]').text == 'Username : Admin'