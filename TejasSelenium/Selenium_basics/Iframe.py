'''
Created on 30-Aug-2025

@author: Admin
'''
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

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

#time.sleep(1000)

#2.navigate to url
driver.get("https://demo.automationtesting.in/Frames.html")

#3.switch tothe single iframe or otherframe
driver.switch_to.frame('SingleFrame')




#4 enter text 
single_iframe_input = driver.find_element(By.TAG_NAME,"input")
single_iframe_input.send_keys("Tejas")
driver.switch_to.default_content()

#5 switch to other frame
#nitin_fame = driver.find_element(By.LINK_TEXT,"Iframe with in an Iframe")
nitin_fame=driver.find_element(By.XPATH,'//a[@href="#Multiple"]')
nitin_fame.click()

driver.switch_to.frame(1)

driver.switch_to.frame(0)

tejasp=driver.find_element(By.TAG_NAME,"input")
tejasp.send_keys("Lord venkatesha")

