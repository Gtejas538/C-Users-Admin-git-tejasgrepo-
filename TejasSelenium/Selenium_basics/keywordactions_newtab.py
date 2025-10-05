'''
Created on 02-Sept-2025

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

#time.sleep(1000)

actions=ActionChains(driver)
#2.navigate to url
driver.get("https://testautomationpractice.blogspot.com/2018/09/automation-form.html")

#3.locate the blog element
blog_element = driver.find_element(By.XPATH, "//a[contains(@href, 'pavantestingtools.com')]")
#4.perform click operation on blog element
actions.move_to_element(blog_element)    
actions.key_down(Keys.CONTROL).click(blog_element).key_up(Keys.CONTROL).perform()

driver.switch_to.window(driver.windows_handles[1])


#blog_element.click()
#actions.key_up(Keys.CONTROL,blog_element).perform()