'''
Created on 03-Sept-2025

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

#3
eleme_1=driver.find_element(By.ID,"field1")
eleme_2=driver.find_element(By.ID,"field2")

# keyword ations
actions.key_down(Keys.CONTROL,eleme_1).send_keys('a').key_up(Keys.CONTROL).perform()

actions.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()

actions.key_down(Keys.CONTROL,eleme_2).send_keys('v').key_up(Keys.CONTROL).perform()


