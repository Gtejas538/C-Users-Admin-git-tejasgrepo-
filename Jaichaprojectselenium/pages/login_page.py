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
        
    def enter_username(self, username):
        self.enter_text(self.username_txtbx_locator, username)
        
    def enter_password(self, password):
        self.enter_text(self.password_txtbx_locator, password)
        
    def click_on_login_btn(self):
        self.click_button(self.login_btn_locator)
        
        