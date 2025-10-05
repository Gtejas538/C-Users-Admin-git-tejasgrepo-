'''
Created on 31-Aug-2025

@author: Admin
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time


# 1. Lauching Chrome Browser with desired capabilities
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("start-maximized")
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(5)

# 2. Navigating to practice site
driver.get("https://testautomationpractice.blogspot.com/2018/09/automation-form.html")

#3 locate the slect tg
color_drop_down=driver.find_element(By.ID, 'colors')

#creaye select class object

select_color=Select(color_drop_down)

select_color.select_by_visible_text("Red")       

select_color.select_by_value("blue")

select_color.select_by_index(2)

time.sleep(5)

#select_color.deselect_all()

select_color.deselect_by_index(0)

time.sleep(5)

select_color.deselect_by_visible_text("Blue")

time.sleep(5)

select_color.deselect_by_value("green")

select_color.deselect_by_index(4)

