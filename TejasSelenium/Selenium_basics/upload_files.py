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

#3.
files_up=driver.find_element(By.XPATH,'//input[@type="file"]')


files_up.send_keys("C:\\Users\\Admin\\Downloads\\Tejas Resume.pdf")
#path1="C:\\Users\\Admin\\Downloads\\Tejas Resume.pdf"
#path2=C:\\Users\\Admin\\Downloads\\SamplePDF.pdf"

rt_x = driver.find_element(By.XPATH, '//button[contains(text(),"Upload Single File")]')
rt_x.click()

mutile_files=driver.find_element(By.ID,"multipleFilesInput")
mutile_files.send_keys("C:\\Users\\Admin\\Downloads\\Tejas Resume.pdf\nC:\\Users\\Admin\\Downloads\\Sumpreeth.pdf"
)
hu=driver.find_element(By.XPATH,'//button[contains(text(),"Upload Multiple Files")]')
hu.click()
