'''
Created on 31-Aug-2025

@author: Admin
'''

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

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
actions=ActionChains(driver)
#time.sleep(1000)

#2.navigate to url
driver.get("https://testautomationpractice.blogspot.com/2018/09/automation-form.html")

#3,
animal_selection=driver.find_element(By.ID,"animals")
select_obj=Select(animal_selection)


select_obj.select_by_index(0)

select_obj.select_by_value('cheetah')

select_obj.select_by_visible_text('Deer')

time.sleep(10)

select_obj.deselect_all()