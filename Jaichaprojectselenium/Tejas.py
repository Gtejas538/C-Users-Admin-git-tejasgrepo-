'''
Created on 11-Oct-2025

@author: Admin
'''
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


@when(u'User clicks on Recruitment tab')
def click_recruitment_tab(context):
    context.login_page_obj.click_on_recruitment_tab()
    

    
@then(u'User should see URL as "{expected_url}"')
def user_get(context, expected_url):
    main_url = context.driver.current_url
    assert expected_url in main_url, f'Expected URL to contain "{expected_url}", but got "{main_url}"'

@when(u'User clicks on Upgrade button')
def click_on_upgrade_button(context):
    context.login_page_obj.click_on_upgrade_tab()
    
@when(u'User enters data in the Vacacny Tab')
def click_on_search_value(context):
    context.login_page_obj.click_on_search_value()
    
    context.base_page_obj.enter_text(context.login_page_obj.vacancy_locator,"Payroll Administrator")
    time.sleep(10)
    context.login_page_obj_page_obj.blur()  
    context.login_page_obj.click_by_search()
    
@then(u'User must be able to see the records down below')
def validate_records(context):
    tejaswi="Records Found"
    baju=context.driver.find_element(By.XPATH,"//span[text()=' (7) Records Found']").text
    assert tejaswi in baju, f'Expected URL to contain "{tejaswi}", but got "{baju}"'
    
    
@when(u'User clicks on Add button')
def click_on_add(context):
    context.login_page_obj.add_button()
    
@then(u'User should see "Add Candidate" text on the page')
def validate_add_candidate(context):
    tejaswi="/addCandidate"
    vivek_sir= context.driver.current_url
    assert tejaswi in vivek_sir, f'Expected URL to contain "{tejaswi}", but got "{vivek_sir}"'
    
    
@when(u'User enters data in the Add Candidate page')
def validate_entering_user_data(context):
    context.login_page_obj.enter_name("Tejaswi")
    

    

    
    
    
    

    
    
    