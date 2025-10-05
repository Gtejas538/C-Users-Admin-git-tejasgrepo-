'''
Created on 07-Sept-2025

@author: Admin
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.common.keys import Keys
from pycparser.c_ast import Break
from selenium.webdriver.support.ui import Select

input_date=input("enter the date in dd/mm/yy")
if not input_date  or len(input_date)!=10 or input_date[2]!="/" or input_date[5]!="/":
    print("please enter the date in correct format")
    exit()
elif int(input_date[0:2])<1 or int(input_date[0:2])>31 or int(input_date[3:5])<1 or int(input_date[3:5])>12 or int(input_date[6:10])>2035 or int(input_date[6:10])<2015:
    print(" Data value out of range please enter the date value ")
    exit()
    


# 1. Lauching Chrome Browser with desired capabilities
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("start-maximized")
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(5)


# 2. Navigating to practice site
driver.get("https://testautomationpractice.blogspot.com/2018/09/automation-form.html")
 

 
 #3 locatedatepicker2
 
#date_picker




date_picker2=driver.find_element(By.ID,"txtDate")
date_picker2.click()


month_select=driver.find_element(By.CLASS_NAME,"ui-datepicker-month")
month_select.click()
for i in range(0,12):
    if i==(int(input_date[3:5])-1):
        select_month=Select(month_select)
        select_month.select_by_index(i)
        
year_select=driver.find_element(By.CLASS_NAME,"ui-datepicker-year")
year_select.click()

for j in range(2015,2036):
    if j==(int(input_date[6:10])):
        select_year=Select(year_select)
        select_year.select_by_value(str(j))

time.sleep(5)    

for z in range(1,32):
    if z==(int(input_date[0:2])):
        date_value = driver.find_element(By.XPATH, f"//table[@class='ui-datepicker-calendar']/tbody/tr/td/a[text()='{z}']")
        date_value.click()

#
#ate=input("enter the date in the form of dd/mm/yy")
#pallaviclass=driver.find_element(By.XPATH,'//table[@class="ui-datepicker-calendar"]/tbody/tr[1]/td[1]')
#pallaviclass.click()

"""# 3. Locate Datepicker2
date_picker2 = driver.find_element(By.ID, 'txtDate')


driver.execute_script("arguments[0].removeAttribute('readonly');",date_picker2)
date_picker2.send_keys("20/09/2025")
"""

# 4. Enter date in date_picker2 using script
#driver.execute_script("arguments[0].value =arguments[1];",date_picker2,"12/09/2025")
