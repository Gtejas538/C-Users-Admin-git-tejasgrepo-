'''
Created on 27-Aug-2025

@author: Admin
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#1.lanauching the browser
tejasw=webdriver.ChromeOptions()
tejasw.add_experimental_option("detach",True)
tejasw.add_argument("--start-maximized")

driver=webdriver.Chrome(options=tejasw)
driver.implicitly_wait(100)

#.navigate to url

driver.get("https://www.amazon.in/ref=cs_503_link/")

#type a element

tab_icon = driver.find_element(By.ID,"twotabsearchtextbox")
tab_icon.send_keys("toothbrush")
tab_press = driver.find_element(By.ID,"nav-search-submit-button")
tab_press.click()

add_cart=driver.find_element(By.ID,"a-autoid-2-announce")
add_cart.click()
time.sleep(5)
goto_cart=driver.find_element(By.LINK_TEXT,"Go to Cart")

driver.switch_to.window(driver.window_handles[0])


goto_cart.click()