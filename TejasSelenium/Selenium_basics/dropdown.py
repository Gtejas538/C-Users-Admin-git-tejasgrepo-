'''
Created on 31-Aug-2025

@author: Admin
'''

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.support.ui import Select
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

#3. we need to locate the select tag element
country_vivek = driver.find_element(By.ID,'country')

#4.create a select class object,
select_country= Select(country_vivek)

select_country.select_by_index(4)

time.sleep(5)

#5.deselect all

#select_country.deselect_by_index(4)
#6. selected by value

select_country.select_by_value('uk')

time.sleep(5)

#7.deselect by value
#select_country.deselect_by_value('uk')

#8. select by vidsible text
select_country.select_by_visible_text('China')

time.sleep(5)





