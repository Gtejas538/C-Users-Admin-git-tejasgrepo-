'''
Created on 02-Sept-2025

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
actions=ActionChains(driver)

#time.sleep(1000)

#2.navigate to url
driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
#3.locaring

locate_us=driver.find_element(By.XPATH,"/html/body/div/section/div/div/div/p/span")
actions.context_click(locate_us).perform()


