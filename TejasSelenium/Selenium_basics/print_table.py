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
 
 #3.to find ccolumns

        
for i in range(2,8):
    for j in range(1,5):
        tejas_element=driver.find_element(By.XPATH,f"//table[@name='BookTable']/tbody/tr[{i}]/td[{j}]")
        table_cell_value=tejas_element.text
        print(table_cell_value, end=" ")
    print()
    
    

        