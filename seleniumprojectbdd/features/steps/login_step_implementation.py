'''
Created on 26-Sept-2025

@author: Admin
'''
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By

@given(u'the browser is launched')
def step_impl(context):
    #1.lauching the browser
    options=webdriver.ChromeOptions()
    options.add_experimental_option("detach",True)
    options.add_argument("start-maximized")
    context.driver=webdriver.Chrome(options=options)
    context.driver.implicitly_wait(5)
        
        #2.navigate to url
        
@when(u'user must be to navigate to the url')
def login(context):
    
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    
@then(u'user must be able to login')
def check_login(context):
    username_txt_bx=context.driver.find_element(By.XPATH,"//input[@name='username']")
    username_txt_bx.send_keys("Admin")
        
    password_txt_bx=context.driver.find_element(By.XPATH,"//input[@name='password']")
    password_txt_bx.send_keys("admin123")
    
    login_btn=context.driver.find_element(By.XPATH,"//button[@type='submit']")
    login_btn.click()
    
    real_url=context.driver.current_url
    expected_url="/dashboard/index"
    assert expected_url in real_url, "login is failed"
    
        
            