'''
Created on 27-Aug-2025

@author: Admin
'''
from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize the WebDriver (e.g., Chrome)
driver = webdriver.Chrome()
driver.get("https://selectorshub.com/xpath-practice-page/") # Replace with the actual URL

# Locate the element using XPath with starts-with()
try:
    element = driver.find_element(By.XPATH, "//input[starts-with(@id, 'dynamic_input_')]")
    element.send_keys("Hello, dynamic field!")
    print("Element found and text entered successfully.")
except Exception as e:
    print(f"Error locating element: {e}")

# Close the browser
driver.quit()