from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("E:\\Automation Essentials\\Jars\\106 chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.implicitly_wait(15)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()

driver.find_element(By.XPATH, "//input[@placeholder='Username']").clear()
driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")

driver.find_element(By.XPATH, "//input[@placeholder='Password']").clear()
driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
driver.find_element(By.XPATH, "//button[text()=' Login ']").click()

expected_title = "OrangeHRM"
actual_title = driver.title
if expected_title == actual_title:
    print("Title is correct")
else:
    print("Title is not correct")

driver.find_element(By.CSS_SELECTOR, "i.oxd-icon.bi-caret-down-fill.oxd-userdropdown-icon").click()
driver.find_element(By.XPATH, "//a[text()='Logout']").click()
driver.close()
