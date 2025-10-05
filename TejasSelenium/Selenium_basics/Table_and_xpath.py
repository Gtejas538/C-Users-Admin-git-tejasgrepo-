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
columns=driver.find_elements(By.XPATH,"//table[@name='BookTable']/tbody/tr/th")
number=len(columns)
print(number)
for i in range(1,number+1):
    column_res=driver.find_element(By.XPATH,f"//table[@name='BookTable']/tbody/tr[1]//*[{i}]")
    print(column_res.text,end=" ")
    
    column_res1=driver.find_element(By.XPATH,f"//table[@name='BookTable']/tbody/tr[2]//*[{i}]")
    print(column_res1.text, end=" ")
    print()

    
