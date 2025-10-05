'''
Created on 19-Sept-2025

@author: Admin
'''

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

#from selenium.webdriver.support.ui import Select
#from selenium.webdriver.support.ui import Select
#select = Select(dropdown_element)    


from selenium.webdriver.common.by import By
import time
#driver = webdriver.Chrome()

#time.sleep(1000)

"""tejas1= webdriver.ChromeOptions()
tejas1.add_experimental_option("detach", True)
driver = webdriver.Chrome(tejas1)"
"""
#1.launching the browser
tejas1=webdriver.ChromeOptions()
tejas1.add_argument("--start-maximized")
tejas1.add_experimental_option("detach", True)

driver=webdriver.Chrome(options=tejas1)
driver.implicitly_wait(20)
actions=ActionChains(driver)
#time.sleep(1000)

#2.navigate to url
driver.get("https://testautomationpractice.blogspot.com/2018/09/automation-form.html")

#3.locate the element
eleme_1=driver.find_element(By.ID,"field1")
eleme_2=driver.find_element(By.ID,"field2")

actions.move_to_element(eleme_1).perform()
time.sleep(3)

actions.move_to_element(eleme_2).perform()
time.sleep(3)

copy_text=driver.find_element(By.XPATH,"//button[text()='Copy Text']")

actions.move_to_element(copy_text).double_click(copy_text).perform()





