'''
Created on 16-Sep-2025

@author: admin
'''
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By



class TestOrangeHRMLoginPage(unittest.TestCase):


    def setUp(self):
        # 1. Lauching Chrome Browser with desired capabilities
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        options.add_argument("start-maximized")
        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(5)
        
        # 2. Navigating to OrangeHRM Login Page
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        


    def tearDown(self):
        self.driver.quit()


    def test_navigation_to_orangehrm_login_page(self):
        # 3. Validating the page title
        expected_title = "OrangeHRM"
        actual_title = self.driver.title
        self.assertEqual(actual_title, expected_title, "Page title is not matching")
        
        # 4. Validating the page url
        expected_url_portion = "/auth/login"
        actual_url = self.driver.current_url
        self.assertIn(expected_url_portion, actual_url, "Current page URL doesn't contain '/auth/login'")
        
    def test_orangehrm_login(self):
        # 3. Enter Username
        username_txt_bx = self.driver.find_element(By.NAME, "username")
        username_txt_bx.send_keys("Admin")
        
        # 4. Enter Password
        password_txt_bx = self.driver.find_element(By.NAME, "password")
        password_txt_bx.send_keys("admin123")
        
        # 5. Click Login Button
        login_btn = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        login_btn.click()
        
        # 6. Validate the successfull Login
        expected_url_portion = "/dashboard/index"
        actual_url = self.driver.current_url
        self.assertIn(expected_url_portion, actual_url, "Login is failed")




if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()