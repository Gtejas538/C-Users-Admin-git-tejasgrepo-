'''
Created on 06-Sept-2025

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
bookn=input("Please enter the book name")

for i in range(2,8):
    tame=driver.find_element(By.XPATH,f"//table[@name='BookTable']/tbody/tr[{i}]/td[1]")
    if tame.text==bookn:
        price=driver.find_element(By.XPATH,f'//table[@name="BookTable"]/tbody/tr[{i}]/td[4]')
        real_price=price.text
        print("the real price is ",real_price)
        
    
#get  from static webelements

