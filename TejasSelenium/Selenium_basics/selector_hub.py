'''
Created on 27-Aug-2025

@author: Admin

'''
from selenium import webdriver
#from selenium.webdriver.support.ui import Select
#from selenium.webdriver.support.ui import Select
#select = Select(dropdown_element)    
import time

from selenium.webdriver.common.by import By
tejas1=webdriver.ChromeOptions()
tejas1.add_argument("--start-maximized")
tejas1.add_experimental_option("detach", True)

driver=webdriver.Chrome(options=tejas1)
driver.implicitly_wait(500)

#time.sleep(1000)

#2.navigate to url
driver.get("https://selectorshub.com/xpath-practice-page/")

#<a style="font-size: 20px; color:blue" href="https://selectorshub.com/wp-content/uploads/2023/12/Mega-sale-600-%C3%97-360-px-30.png" download=""> Click to Download PNG File </a>
#preethamg=driver.find_element(By.XPATH,"//a[@href='https://selectorshub.com/wp-content/uploads/2023/12/Mega-sale-600-%C3%97-360-px-30.png']")                                  
#preethamg.click()

#sriharig = driver.find_element(By.XPATH,"//button[text()='windowAlertFunction']")
#sriharig.click()

#mass_j=driver.find_element(By.XPATH,"//button[@class='dropbtn']")
#mass_j.click()

jai_it=driver.find_element(By.XPATH,"//input[contains(@title,'first crush)]")
jai_it.click()
