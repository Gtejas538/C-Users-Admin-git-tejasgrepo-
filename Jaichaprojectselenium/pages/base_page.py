'''
Created on 04-Oct-2025

@author: Admin

'''
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout=10)
        
    def navigate_to_page(self, url):
        self.driver.get(url)
        
    def enter_text(self, locator, text):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.send_keys(text)
        
    def click_button(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
        
    def get_current_page_url(self):
        current_page_url = self.driver.current_url
        return current_page_url
                                  
        
    
