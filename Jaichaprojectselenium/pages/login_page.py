'''
Created on 04-Oct-2025

@author: Admin
'''


from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.username_txtbx_locator = (By.NAME, "username")
        self.password_txtbx_locator = (By.NAME, "password")
        self.login_btn_locator = (By.XPATH, "//button[@type='submit']")
        self.recruitment_tab_locator=(By.LINK_TEXT, "Recruitment")
        self.recruitment_page_title="Recruitment"
        self.upgrade_tab_locator =(By.LINK_TEXT, "Upgrade")
        self.vacancy_locator=(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div/div[1]")
        self.blur_locator=(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div/div[1]")
        self.search_value_locators=(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div/div[1]")
        self.payroll_admin=(By.XPATH,"//div[@role='option']/span[text()='Payroll Administrator']")
        self.edit_locator=(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div/div[1]/div/div/div[2]/div[1]/div/div[2]")
        self.search1_locator=(By.XPATH,"//button[text()=' Search ']")
        #self.result_records=(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/span")
        self.add_locator=(By.XPATH,"//button[text()=' Add ']")
        self.name_locator=(By.NAME,"firstName")
        self.second_locator=(By.NAME,"lastName")
        self.email_locator=(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div[1]/div/div[2]/input")
        self.job_title=(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div[1]/div[1]")
        self.enter_jobtitle=(By.XPATH,"//div[@role='option']/span[text()='Chief Technical Officer']")
        self.status_locator=(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[4]/div/div[2]/div/div/div[1]")
        self.status_going=(By.XPATH,"//div[@role='option']/span[text()='Application Initiated']")
        self.reset_button=(By.XPATH,"//button[text()=' Reset ']")
        self.validate_pyroll=(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div/div[1]/div/div/div[2]/div[1]/div/div[2]")
        
    def enter_username(self, username):
        self.enter_text(self.username_txtbx_locator, username)
        
    def enter_password(self, password):
        self.enter_text(self.password_txtbx_locator, password)
        
    def click_on_login_btn(self):
        self.click_button(self.login_btn_locator)
        
    def click_on_recruitment_tab(self):
        self.click_button(self.recruitment_tab_locator)
        
    def user_recruitment_title(self):
        
        self.get_current_page_title(self.recruitment_page_title)
        
    def click_on_upgrade_tab(self):
        self.click_button(self.upgrade_tab_locator)
        
        
    def click_on_search_value(self):
        self.click_button(self.vacancy_locator)
    
    def click_on_payroll(self):
        self.click_button(self.payroll_admin)
        
        
    def click_by_search(self):
        self.click_button(self.search1_locator)
        
    
    def add_button(self):
        self.click_button(self.add_locator)
        
    def enter_name(self,name):
        self.click_button(self.name_locator)
        self.enter_text(self.name_locator,name)
        
    def enter_second_name(self,secondname):
        self.click_button(self.second_locator)
        self.enter_text(self.second_locator,secondname)    
        
    def enter_email(self,email):
        self.click_button(self.email_locator)
        self.enter_text(self.email_locator,email)
        
    def click_on_job_title(self):
        self.click_button(self.job_title)
        
    def click_on_enter_jobtitle(self):
        self.click_button(self.enter_jobtitle)
        
       
    def click_on_status(self):
        self.click_button(self.status_locator)
    def click_on_status_going(self):
        self.click_button(self.status_going)
        
    def click_on_reset(self):
        self.click_button(self.reset_button)
        
    def click_on_edit(self):
        self.click_button(self.edit_locator)