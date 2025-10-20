'''
Created on 24-Sep-2025

@author: admin
'''
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.recruitment_page import RecruitmentPage
import time

@given(u'Chrome browser is launched')
def launch_chrome_browser(context):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_argument("start-maximized")
    context.driver = webdriver.Chrome(options=options)
    # context.driver.implicitly_wait(5)
    context.base_page_obj = BasePage(context.driver)
    context.login_page_obj = LoginPage(context.driver)
    context.recruitment_page_obj = RecruitmentPage(context.driver)
    
    all_window_handles = context.driver.window_handles


@when(u'User navigates to OrangeHRM Login Page')
def navigate_to_login_page(context):
    # context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    context.base_page_obj.navigate_to_page("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")


@then(u'User should see page title as OrangeHRM')
def validate_login_page_title(context):
    expected_title = "OrangeHRM"
    actual_title = context.driver.title
    assert actual_title == expected_title, "Page title is not matching"
    
@when(u'User enters Username')
def enter_username(context):
    # username_txt_bx = context.driver.find_element(By.NAME, "username")
    # username_txt_bx.send_keys("Admin")
    
    context.login_page_obj.enter_username("Admin")


@when(u'User enters Password')
def enter_password(context):
    # password_txt_bx = context.driver.find_element(By.NAME, "password")
    # password_txt_bx.send_keys("admin123")
    
    context.login_page_obj.enter_password("admin123")

@when(u'User clicks on Login button')
def click_on_login_button(context):
    # login_btn = context.driver.find_element(By.XPATH, "//button[@type='submit']")
    # login_btn.click()
    
    context.login_page_obj.click_on_login_btn()


@then(u'User should see "/dashboard/index" in the current page URL')
def validate_dashboard_url(context):
    expected_url_portion = "/dashboard/index"
    # actual_url = context.driver.current_url
    actual_url = context.base_page_obj.get_current_page_url()
    # print("actual_url:", actual_url)
    # print(type(actual_url))
    assert expected_url_portion in actual_url, "Login is failed"
    
@when(u'User enters Username "{username}"')
def enter_username_paramter(context, username):
    # username_txt_bx = context.driver.find_element(By.NAME, "username")
    # username_txt_bx.send_keys(username)
    
    context.login_page_obj.enter_username(username)
    
@when(u'User enters Password "{password}"')
def enter_password_paramter(context, password):
    # password_txt_bx = context.driver.find_element(By.NAME, "password")
    # password_txt_bx.send_keys(password)
    
    context.login_page_obj.enter_password(password)
    

    
