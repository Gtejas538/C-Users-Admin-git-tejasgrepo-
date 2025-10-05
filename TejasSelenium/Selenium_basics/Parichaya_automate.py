'''
Created on 30-Aug-2025

@author: Admin
'''


from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

#from selenium.webdriver.support.ui import Select
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
driver.get("https://parichaya.co/")

#3. click to login
"""
parichaya_login = driver.find_element(By.CLASS_NAME,"header-login-btn")
parichaya_login.click()


Parichaya_user=driver.find_element(By.ID,"login-user-login")
Parichaya_user.send_keys("Vok001330")

parichaay_password = driver.find_element(By.ID,"login-user-password")
parichaay_password.send_keys("tej@97")

login_info=driver.find_element(By.XPATH,"html/body/div[2]/div/div[2]/div[2]/div/form/input[4]")
login_info.click()


Home_icon = driver.find_element(By.XPATH,'/html/body/div[1]/header/div/div[2]/nav/div/ul/li[1]/a')
Home_icon.click()

"""

Woman_search = driver.find_element(By.NAME,"seeking")
Woman_search.send_keys("Woman")
Woman_search.click()

Age_from=driver.find_element(By.NAME,"age_from")
Age_from.send_keys("23")
Age_from.click()

Age_to=driver.find_element(By.NAME,"age_to")
Age_to.send_keys("27")
Age_to.click()

Search_button=driver.find_element(By.XPATH,'//input[@class="dsp_submit_button dspdp-btn dsp-block dspdp-btn-default"]')
Search_button.click()




