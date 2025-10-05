'''
Created on 07-Sept-2025

@author: Admin
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.common.keys import Keys
from pycparser.c_ast import Break

# 1. Lauching Chrome Browser with desired capabilities
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("start-maximized")
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(5)

# 2. Navigating to practice site
driver.get("https://testautomationpractice.blogspot.com/2018/09/automation-form.html")
 
#3.
rows = len(driver.find_elements(By.XPATH, "//table[@name='BookTable']/tbody/tr"))

for i in range(1, rows+1):
    book = driver.find_element(By.XPATH, f'//table[@name="BookTable"]/tbody/tr[{i}]/*[1]').text
    price_rows = len(driver.find_elements(By.XPATH, "//table[@name='BookTable']/tbody/tr"))

for i in range(1, rows+1):
    book = driver.find_element(By.XPATH, f'//table[@name="BookTable"]/tbody/tr[{i}]/*[1]').text
    price = driver.find_element(By.XPATH, f'//table[@name="BookTable"]/tbody/tr[{i}]/*[4]').text
    print(f"{book:<25} | {price}")
 
 