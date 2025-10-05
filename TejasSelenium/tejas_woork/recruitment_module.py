'''
Created on 15-Sep-2025

@author: admin
'''
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By



class TestOrangeHRmloginfeature(unittest.TestCase):
    def test_logging_to_the_orangehrm_loginpage(self):
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
        
        #validate the succesful login
        page_url=driver.current_url
        expected_url="dashboard/index"
        
        self.assertIn(expected_url,page_url,"url is not found")
        print("url is found successfully")
        
    def test__the_accessto_recruitment_module(self):
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
        #6. click on the recruitment module
        recruitment_case=driver.find_element(By.XPATH,"//span[text()='Recruitment']")
        recruitment_case.click()
        
        #7. validate the recruitment page
        self.assertTrue(recruitment_case, "recruitment module is not found")
        
    def test_taband_details_seen(self):
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
        #6. click on the recruitment module
        recruitment_case=driver.find_element(By.XPATH,"//span[text()='Recruitment']")
        recruitment_case.click()
        
        #7. validate the recruitment page
        actual_url=driver.current_url
        expected_url="recruitment/viewCandidates"
        
        self.assertIn(expected_url, actual_url,"cant access the recruitment page")
        
        


    def test_upgrade_button(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        options.add_argument("start-maximized")
        driver = webdriver.Chrome(options=options)
        driver.implicitly_wait(5)

        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

        driver.find_element(By.NAME, "username").send_keys("Admin")
        driver.find_element(By.NAME, "password").send_keys("admin123")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()

        upgrade_button = driver.find_element(By.XPATH, "//header//a/button")
        upgrade_button.click()

        window_handles_list = driver.window_handles
        driver.switch_to.window(window_handles_list[1])

        actual_url = driver.current_url
        expected_url = "/open-source/upgrade-to-advanced"
        self.assertIn(expected_url, actual_url, "Upgrade page is not found")

        driver.quit()

        
        
if __name__ == "__main__":
    import sys;sys.argv = ['', 'Test.testName']
    unittest.main()