'''
Created on 06-Sept-2025

@author: Admin
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.common.keys import Keys
from pycparser.c_ast import Break

# 1. Lauching Chrome Browser with desired capabilities
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("start-maximized")
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(5)

# 2. Navigating to practice site
driver.get("https://testautomationpractice.blogspot.com/2018/09/automation-form.html")

actions=ActionChains(driver)
#3 clicking on the pages
"""
pagecount=5

for i in range(1,pagecount):
    page_ondu=driver.find_element(By.XPATH,f"//ul[@class='pagination']/li[{i}]")
   
    time.sleep(2)
    page_ondu.click()
   """ 
flag=False
longlive=input("enter the element name whose price we need to find ")

viveka=driver.find_elements(By.XPATH,"//ul[@class='pagination']/li")
page_count=int(len(viveka))
print("The count is ",page_count)


for r in range(1,page_count+1):
        page_poo=driver.find_element(By.XPATH,f"//ul[@class='pagination']/li[{r}]")
        page_poo.click()
        for z in range(1,6):
            element_name = driver.find_element(By.XPATH,f"//table[@id='productTable']/tbody/tr{[z]}/td[2]")
            if longlive==element_name.text:
                chef=driver.find_element(By.XPATH,f"//table[@id='productTable']//tbody/tr{[z]}/td[3]")
                print("the price of the element is ",chef.text)
                flag=True
                if flag==True:
                    break



    
    



