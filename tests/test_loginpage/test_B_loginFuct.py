import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

def test_incorrectUsername(driver_Inst):
    driver_Inst.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input').send_keys("AdminA")
    driver_Inst.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input').send_keys("admin123")
    driver_Inst.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
    assert driver_Inst.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/p').text == "Invalid credentials"

def test_incorrectPassword(driver_Inst):
    driver_Inst.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input').send_keys("Admin")
    driver_Inst.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input').send_keys("admin1233")
    driver_Inst.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
    assert driver_Inst.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/p').text == "Invalid credentials"

def test_emptyUsernamePassword(driver_Inst):
    driver_Inst.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input').send_keys("")
    driver_Inst.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input').send_keys("")
    driver_Inst.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
    assert driver_Inst.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/span').text == "Required"

def test_correctUsernamePassword(driver_Inst):
    driver_Inst.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input').send_keys("Admin")
    driver_Inst.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input').send_keys("admin123")
    driver_Inst.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
    time.sleep(5)