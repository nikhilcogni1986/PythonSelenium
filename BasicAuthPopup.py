from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("E:\\Automation Essentials\\Jars\\106 chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.implicitly_wait(15)
driver.get("https://admin:admin@the-internet.herokuapp.com/digest_auth")
driver.maximize_window()
digest_auth = driver.find_element(By.XPATH, "//p[contains(text(),'Congratulations! You must have the proper credenti')]")
if digest_auth.is_displayed():
    print("Logged in successful!!")
else:
    print("Unable to login")