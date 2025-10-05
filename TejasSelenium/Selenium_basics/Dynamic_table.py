from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.common.keys import Keys
from pycparser.c_ast import Break

# 1. Lauching Chrome Browser with desired capabilities
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("start-maximized")
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(5)

# 2. Navigating to practice site
driver.get("https://testautomationpractice.blogspot.com/2018/09/automation-form.html")
 
tejas_input = input("Enter the browser name:")
for z in range(1,5):
    shreyas_output = driver.find_element(By.XPATH, f'//tbody[@id="rows"]/tr[{z}]/td[1]')
    jacob = shreyas_output.text
    if tejas_input == jacob:
        dinesh = int(input("""Choose an feature :1-Network (Mbps)
                                                2- Memory (MB)
                                                3- CPU (%)
                                                4- Disk (MB/s)"""))
        match dinesh:
            case 1:
                network = driver.find_element(By.XPATH, f'//*[@id="rows"]/tr[{z}]/td[1]//following-sibling::td[contains(text(),"Mbps")]')
                network_val = network.text
                print("The Network speed for  is:", network_val)
            case 2:
                    memory = driver.find_element(By.XPATH, f'//tbody[@id="rows"]/tr[{z}]/td[1]/following-sibling::td[contains(text(),"MB") and not(contains(text(),"/s"))]')
                    memory_val = memory.text
                    print("The Memory  is:", memory_val)
            case 3:
                    cpu = driver.find_element(By.XPATH, f'//*[@id="rows"]/tr[{z}]/td[1]//following-sibling::td[contains(text(),"%")]')
                    cpu_val = cpu.text
                    print("The cpu percentage usage is:", cpu_val)
            case 4:
                    disk = driver.find_element(By.XPATH, f'//*[@id="rows"]/tr[{z}]/td[1]//following-sibling::td[contains(text(),"MB/s")]')
                    disk_val = disk.text
                    print("The disk usage  is:", disk_val)
            case _:
                    print("Please Enter valid choice and try again")