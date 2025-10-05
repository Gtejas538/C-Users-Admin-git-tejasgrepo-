'''
Created on 27-Aug-2025

@author: Admin
'''

from selenium import webdriver
#from selenium.webdriver.support.ui import Select
#from selenium.webdriver.support.ui import Select
#select = Select(dropdown_element)    
from selenium.webdriver.common.action_chains import ActionChains
import time

from selenium.webdriver.common.by import By
tejas1=webdriver.ChromeOptions()
tejas1.add_argument("--start-maximized")
tejas1.add_experimental_option("detach", True)

driver=webdriver.Chrome(options=tejas1)
driver.implicitly_wait(20)

#time.sleep(1000)

#2.navigate to url
driver.get("https://demo.automationtesting.in/Resizable.html")

#retejas=driver.find_element(By.XPATH,"//td[text()='Home']")
#retejas.click()
#jtejas.click()

#vivek_great=driver.find_element(By.XPATH,"//a[contains(@href,'WYSIWYG')]")
#vivek_great.click()

#3 create oject of actionchains class
actions=ActionChains(driver)
#4.scroll 

#actions.scroll_by_amount(0, 1000).perform()
"""
r_element=driver.find_element(By.XPATH,"//a[@href='Interactions.html']")
actions.move_to_element(r_element).perform()

yu_element=driver.find_element(By.XPATH,"/html/body/header/nav/div/div[2]/ul/li[6]/ul/li[1]/a")
actions.move_to_element(yu_element).perform()

z_element=driver.find_element(By.XPATH,'//a[@href="Static.html"]')
z_element.click()

"""

time.sleep(10)
zoom_element=driver.find_element(By.XPATH,"//div[contains(@class,'ui-resizable-handle ui-resizable-se')]")
actions.click_and_hold(zoom_element).move_by_offset(100,100).release().perform()









