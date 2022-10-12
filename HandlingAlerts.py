from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("E:\\Automation Essentials\\Jars\\106 chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.implicitly_wait(15)
driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")
driver.maximize_window()

btnAlert = driver.find_element(By.XPATH, "//input[@name='alert']")
btnAlert.click()
alert = driver.switch_to.alert
print(alert.text)
alert.accept()

# prompt alert text box
prompt_alert = driver.find_element(By.XPATH, "//input[@name='prompt']")
prompt_alert.click()
alert_prompt = driver.switch_to.alert
print(alert_prompt.text)
alert_prompt.send_keys("Welcome")
alert_prompt.accept()

