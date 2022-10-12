from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("E:\\Automation Essentials\\Jars\\106 chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
driver.implicitly_wait(15)
driver.maximize_window()

email_text = driver.find_element(By.XPATH, "//input[@id='Email']").get_attribute("value")
print(email_text)
driver.close()
