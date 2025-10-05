'''
Created on 31-Aug-2025

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
driver.get("https://demo.automationtesting.in/Frames.html")

#3.switch to the dingle frame it switches the focus t the specified frame using name index webe;emt

driver.switch_to.frame("SingleFrame")

#enter textin pinput foekd
single_frame=driver.find_element(By.TAG_NAME,"input")
single_frame.send_keys("Jai hind")

#switch to the next tag
driver.switch_to.default_content()

#switch t o ther frame by xpath
other_frame=driver.find_element(By.XPATH,'//*[@id="#Multiple"/iframe')
driver.switch_to.frame(other_frame)

tejas_frame=driver.find_element(By.TAG_NAME,"iframe")
driver.switch_to.frame(tejas_frame)

last_frame=driver.find_element(By.TAG_NAME,"input")
last_frame.send_keys("Intelligen")

driver.switch_to.default_content()





