'''
Created on 27-Sept-2025

@author: Admin
'''


from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By

@given(u'Chrome browser is launched')
def launch_chrome_browser(context):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_argument("start-maximized")
    context.driver = webdriver.Chrome(options=options)
    context.driver.implicitly_wait(5)


@when(u'User navigates to OrangeHRM Login Page')
def navigate_to_login_page(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")


@then(u'User should see page title as OrangeHRM')
def validate_login_page_title(context):
    expected_title = "OrangeHRM"
    actual_title = context.driver.title
    assert actual_title == expected_title, "Page title is not matching"
    
@when(u'User enters Username')
def enter_username(context):
    username_txt_bx = context.driver.find_element(By.NAME, "username")
    username_txt_bx.send_keys("Admin")


@when(u'User enters Password')
def enter_password(context):
    password_txt_bx = context.driver.find_element(By.NAME, "password")
    password_txt_bx.send_keys("admin123")

@when(u'User clicks on Login button')
def click_on_login_button(context):
    login_btn = context.driver.find_element(By.XPATH, "//button[@type='submit']")
    login_btn.click()


@then(u'User should see /dashboard/index in the current page URL')
def validate_dashboard_url(context):
    expected_url_portion = "/dashboard/index"
    actual_url = context.driver.current_url
    assert expected_url_portion in actual_url, "Login is failed"
    
@when(u'User enters username "{username}"')
def enter_username_paramter(context, username):
    username_txt_bx = context.driver.find_element(By.NAME, "username")
    username_txt_bx.send_keys(username)
    
@when(u'User enters password "{password}"')
def enter_password_paramter(context, password):
    password_txt_bx = context.driver.find_element(By.NAME, "password")
    password_txt_bx.send_keys(password)
    
@then(u'User should see "{url}" in the current page URL')
def validate_dashboard_url_parameter(context, url):
    expected_url_portion = url
    actual_url = context.driver.current_url
    assert expected_url_portion in actual_url, "Login is failed"