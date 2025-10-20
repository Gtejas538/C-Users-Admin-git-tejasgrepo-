'''
Created on 11-Oct-2025

@author: Admin
'''
'''
Created on 04-Oct-2025

@author: Admin
'''


from pages.base_page import BasePage
from pages.login_page import LoginPage

from selenium.webdriver.common.by import By

class RecruitmentPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.recruitment_tab_locator=(By.LINK_TEXT, "Recruitment")
        self.recruitment_page_title="Recruitment"
        self.upgrade_tab_locator =(By.LINK_TEXT, "Upgrade")
        
        self.search_value_locators=(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div")
        self.payroll_admin=(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div[2]/div[7]/span")
        self.search1_locator=(By.XPATH,"//button[text()=' Search ']")
        self.result_records=(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/span")
        self.add_locator=(By.XPATH,"//button[text()=' Add ']")
        self.name_locator=(By.NAME,"firstName")
        
        
        
        
    
    def click_on_recruitment_tab(self):
        self.click_button(self.recruitment_tab_locator)
        
    def user_recruitment_title(self):
        
        self.get_current_page_title(self.recruitment_page_title)
        
    def click_on_upgrade_tab(self):
        self.click_button(self.upgrade_tab_locator)
        
        
    def click_on_search_value(self):
        self.click_button(self.search_value_locators)
    
    def click_by_search(self):
        self.click_button(self.search1_locator)
        
    def click_on_payroll(self):
        self.click_button(self.payroll_admin)
    
    def add_button(self):
        self.click_button(self.add_locator)
        
    def enter_name(self, name):
        self.click_button(self.name_locator)
        self.enter_text(self.name_locator,name)
        
            
        
        
        
        
        
        
        
        
            
        
        