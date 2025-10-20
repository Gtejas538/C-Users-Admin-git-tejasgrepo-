'''
Created on 11-Oct-2025

@author: Admin
'''
from token import EQUAL
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
    
    context.base_page_obj.enter_text(context.login_page_obj.search_value_locators,"Payroll Administrator")
    context.login_page_obj.click_on_payroll()
    time.sleep(10) 
    context.login_page_obj.click_by_search()
    
    
    
@when(u'User clicks on Add button')
def click_on_add(context):
    context.login_page_obj.click_button(context.login_page_obj.add_locator)
    
@then(u'User should see "Add Candidate" text on the page')
def validate_add_candidate(context):
    tejaswi="/addCandidate"
    vivek_sir= context.driver.current_url
    assert tejaswi in vivek_sir, f'Expected URL to contain "{tejaswi}", but got "{vivek_sir}"'
    
    
@when(u'User enters data in the Add Candidate page')
def validate_entering_user_data(context):
    context.login_page_obj.enter_name("Tejaswi")
    
    
@when(u'Users enters the second name')
def enter_second_name(context):
    context.login_page_obj.enter_second_name("Gowda")
    time.sleep(5)
    
@when(u'User enter the email id')
def enter_email(context):
    context.login_page_obj.enter_email("tg@gmail.com")
    
@then(u'User clicks on Save button')
def validate_clicking_on_save_button(context):
    context.base_page_obj.click_button((By.XPATH,"//button[text()=' Save ']"))

@then(u'User must see records found')
def validate_records_found(context):
    jessica="Tejaswi"
    baju=context.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div/div[1]/div[1]/div/div/div[2]").text
    assert jessica in baju, f'Expected URL to contain "{jessica}", but got "{baju}"'
    
@then(u'User must be able to see the added candidate in the list')
def validate_added_candidate(context):
    tejaswi="Tejaswi"
    baju=context.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div/div[1]/div[1]/div/div/div[2]").text
    assert tejaswi in baju, f'Expected URL to contain "{tejaswi}", but got "{baju}"'
    
@when(u'User enters all the  data in the Candidates Tab')
def click_on_job_title(context):
    context.login_page_obj.click_on_job_title()
    context.base_page_obj.enter_text(context.login_page_obj.job_title,"Chief Technical Officer")
    context.login_page_obj.click_on_enter_jobtitle()
    
    
@when(u'User enters the second data')
def enter_second_data(context):
    context.login_page_obj.click_on_status()
    context.base_page_obj.enter_text(context.login_page_obj.status_locator,"Application Initiated")
    context.login_page_obj.click_on_status_going()


@then(u'User clicks on Reset button')
def validate_clicking_on_reset_button(context):
    context.login_page_obj.click_on_reset()
    
@then(u'All the fields should be reset to default values')
def validate_reset_fields(context):
    result1=context.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/div[1]").text
    assert result1=="-- Select --", f'Expected URL to contain "-- Select --", but got "{result1}"'
    
    result2=context.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[4]/div/div[2]/div/div/div[1]").text 
    assert result2=="-- Select --", f'Expected URL to contain "-- Select --", but got "{result2}"'
    
@then(u'User must be able to validate the records')
def validate_records_payn(context):
    jk="Payroll"
    bs=context.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div/div[1]/div/div/div[2]/div[1]/div/div[1]//following-sibling::div[text()='Payroll Administrator']").text
    assert jk in bs, f'Expected URL to contain "{jk}", but got "{bs}"'
    
@then(u'User clicks on Edit button')
def validate_clicking_on_edit_button(context):
    context.login_page_obj.click_on_edit()

    
  