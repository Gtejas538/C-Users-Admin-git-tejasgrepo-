'''
Created on 27-Aug-2025

@author: Admin
'''
from gettext import find
'''
Created on 27-Aug-2025

@author: Admin
'''
'''
Created on 15-Aug-2025

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
driver.get("https://testautomationpractice.blogspot.com/2018/09/automation-form.html")

#3. typing a element

tejasname = driver.find_element(By.ID,'name')
tejasname.send_keys('Vivek')

radiobox = driver.find_element(By.CLASS_NAME,'form-check-input')
radiobox.click()

#<input class="form-check-input" id="sunday" type="checkbox" value="sunday">
list23=["sunday","monday","tuesday","wednesday","thursday","friday","saturday"]
for item in list23:
    sunday1=driver.find_element(By.ID,item)
    sunday1.click()
    
color0 = driver.find_element(By.XPATH, "//option[@value='blue']//following-sibling::option[@value='red']")
color0.click()    
    
#color1=driver.find_element(By.XPATH,'//option[@value="blue"]')
#color1.click()

#<option value="red"> Red </option>
"""
color0=driver.find_element(By.XPATH,'(//option[@value="red"])[1]')
color0.click()

color2=driver.find_element(By.XPATH,'(//option[@value="red"])[2]')
color2.click()
"""
#country_item=driver.find_element(By.ID,"country")
#country_item.send_keys("Canada")
#select_object = Select(country_item)
#select_object.select_by_value("canada")
#

#datee_picker=driver.find_element(By.ID,"datepicker")
#datee_picker.send_keys("15/08/2025")

#datee_picker1=driver.find_element(By.ID,"txtDate")
#datee_picker1.send_keys("19/08/2025")
#alert
#alert_button=driver.find_element(By.XPATH,"//button[text()='Simple Alert']")

#alert_button.click()
    
#days_element=driver.find_element(By.CSS_SELECTOR,"#post-body-1307673142697428135 > div:nth-child(11) > label")
#days_element.click()

#dropdown_element = driver.find_element_by_id("Red") # Or By.xpath, By.name, etc.

#search_element = driver.find_element(By.ID,'Wikipedia1_wikipedia-search-input')
#search_element.send_keys('selenium')
#search_button= driver.find_element(By.CLASS_NAME,'wikipedia-search-button')
#search_button.click()

#Search_result=driver.find_element(By.LINK_TEXT,'Selenium (software)')
#Search_result.click()
#Search_result1=driver.find_element(By.XPATH,"/html/body/div[3]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[4]/div[3]/div/aside/div/div[1]/div[1]/div[2]/div[3]/a")
    # Example using Selenium with Python
#driver.execute_script("arguments[0].removeAttribute('target')", Search_result1)
#Search_result1.click()
#driver.switch_to.window(driver.window_handles[1])

#tejase_result=driver.find_element(By.XPATH,"/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/p[2]/a[2]" )
#teja_result=driver.find_element(By.LINK_TEXT, "browser automation")
#teja_result.click()
#prajy_res=driver.find_element(By.LINK_TEXT,"Selenium IDE")
#prajy_res.click()

#.switch_to.window(driver.window_handles[2])
#tejase_result=driver.find_element(By.XPATH,"/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/p[2]/a[2]" )
#tejase_result.click()
#driver.switch_to.window(driver.window_handles[0])
#button_element = driver.find_element(By.XPATH, "//button[text()='Simple Alert']")
#button_element.click()
"""time.sleep(5)
driver.switch_to.alert.accept()

button_element1 = driver.find_element(By.XPATH, "//button[text()='Confirmation Alert']")
button_element1.click()
time.sleep(5)
driver.switch_to.alert.dismiss()

button_element2 = driver.find_element(By.XPATH, "//button[text()='Prompt Alert']")
button_element2.click()
driver.switch_to.alert.send_keys("Vivek Sir")
driver.switch_to.alert.accept()

button_element89 = driver.find_element(By.XPATH, "//button[text()='New Tab']")
button_element89.click()
driver.switch_to.window(driver.window_handles[0])


"""



#mouse_hover=driver.find_element(By.XPATH,"//button[text()='Point Me']")

#mouse_hover.send_keys("Laptops")
#mouse_hover.click()

copy_text_button=driver.find_element(By.XPATH,"//button[text()='Copy Text']")
actions = ActionChains(driver)
actions.double_click(copy_text_button).perform()


time.sleep(7)

drag_element=driver.find_element(By.XPATH,"//div[@id='draggable']")
target_element=driver.find_element(By.XPATH,"//div[@id='droppable']")
actions.drag_and_drop(drag_element, target_element).perform()

time.sleep(7)

slider1=driver.find_element(By.XPATH,"//span[contains(@class,'ui-slider-handle ui-corner')]")

actions.click_and_hold(slider1).move_by_offset(100,0).release().perform()

slider2=driver.find_element(By.XPATH,"//span[@style='left: 60%;']")
actions.click_and_hold(slider2).move_by_offset(100,0).release().perform()

new_feature=driver.find_element(By.XPATH,"//button[text()='New Tab']")
new_feature.click()
#slider2=driver.find_element(By.XPATH,("/html/body/div[3]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[4]/div[3]/div/aside/div/div[9]/div[1]/div/span[1]"))[2]

#actions.click_and_hold(slider2).move_by_offset(100,0).release().perform()



