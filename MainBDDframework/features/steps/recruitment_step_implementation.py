'''
Created on 28-Sept-2025

@author: Admin
'''
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By

@given(u'Launching the browser')
def step1_implementation(context):
    context.driver=webdriver.ChromeOptions()
    context.driver.add_experimental_option("detach",True)
    context.driver.add_argument("start-maximized")
    context.driver=webdriver.Chrome(options=context.driver)
    
    context.driver.implicitly_wait(5)
    
@when(u'later navigating to the url')
def navigate_url(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    
@when(u'user enters the username "<username>"')
def enter_username(context,username):
    username_txt_bx=context.driver.find_element(By.NAME,"username")
    username_txt_bx.send_keys(username)
    
@when(u'user enters the password "<password>"')
def enter_password(context,password):
    password_txt_bx=context.driver.find_element(By.NAME,"password")
    password_txt_bx.send_keys(password)
    
@then(u'user is logged in')
def user_login(context,expected_url):
    login_btn=context.driver.find_element(By.XPATH,"//button[@type='submit']")
    login_btn.click()
    
    
    actual_url=context.driver.current_url
    assert expected_url in actual_url, "Login is failed"
    
    