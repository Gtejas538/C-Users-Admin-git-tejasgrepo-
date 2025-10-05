'''
Created on 07-Sept-2025

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
driver.get("https://testautomationpractice.blogspot.com/2018/09/automation-form.html")

#3.locate the shadow host
shadow_host=driver.find_element(By.ID,"shadow_host")

#4.get the shadow root
first_shadow_root=shadow_host.shadow_root

#5locate elemnt in shadow do using shadow root
tejas=first_shadow_root.find_element(By.CSS_SELECTOR,"input[type=text]:nth-child(5)")
tejas.send_keys("long live vivek sir ")

