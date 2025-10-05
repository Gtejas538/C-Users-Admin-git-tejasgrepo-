'''
Created on 15-Sept-2025

@author: Admin
'''
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class Test_the_navigation_url(unittest.TestCase):

    
    def test_the_navigation_url(self):
        from selenium import webdriver
        from selenium.webdriver.common.by import By
        # 1. Lauching Chrome Browser with desired capabilities
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        options.add_argument("start-maximized")
        driver = webdriver.Chrome(options=options)
        driver.implicitly_wait(5)

    # 2. Navigating to practice site
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
         
        tejas=driver.find_element(By.XPATH,"//button[text()=' Login ']")
        self.assertTrue(tejas,"its not true ")
        
        John=driver.find_element(By.XPATH,"//h5[text()='Login']")
        self.assertTrue(John," john is invalid")   
    #3. to validate the url
        
        expected_url="/auth/login"
        actual_url=driver.current_url
        self.assertIn(expected_url,actual_url,"Current page URL doesn't contain '/auth/login'")
        
    #4 validation
        expected_title="OrangeHRM"
        actual_title=driver.title
        self.assertEqual(expected_title, actual_title, "Page title is not matching")
        
        
    def test_orangehrm_login(self):
        # 1. Lauching Chrome Browser with desired capabilities
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        options.add_argument("start-maximized")
        driver = webdriver.Chrome(options=options)
        driver.implicitly_wait(5)
      
        
        # 2. Navigating to OrangeHRM Login Page
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        
        # 3. Enter Username
        username_txt_bx = driver.find_element(By.NAME, "username")
        username_txt_bx.send_keys("Admin")
        
        # 4. Enter Password
        password_txt_bx = driver.find_element(By.NAME, "password")
        password_txt_bx.send_keys("admin123")
        
        # 5. Click Login Button
        login_btn = driver.find_element(By.XPATH, "//button[@type='submit']")
        login_btn.click()
        #validate the successfull Login
        
        dashboard_element=driver.find_element(By.XPATH,"//span[text()='Dashboard']")
        self.assertTrue(dashboard_element.is_displayed(),"dashboard is not displayed")
        
      

if __name__ == "__main__":
    import sys;sys.argv = ['','Test_the_navigation_url.test_orangehrm_login']
    unittest.main()