from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("E:\\Automation Essentials\\Jars\\106 chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.implicitly_wait(15)
driver.get("https://itera-qa.azurewebsites.net/home/automation")
driver.maximize_window()

checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox' and contains(@id,'day')]")
print(len(checkboxes))

for i in range(len(checkboxes)):
    checkboxes[i].click()


# select the last 2 checkboxes
for i in range(len(checkboxes)-2, len(checkboxes)):
    checkboxes[i].click()

# selection based on week name input
for checkbox in checkboxes:
    week_name = checkbox.get_attribute('id')
    print(week_name)
    if week_name == 'monday' or week_name == 'saturday':
        checkbox.click()

# select the first check boxes
for i in range(len(checkboxes)):
    if i < 2:
        checkboxes[i].click()

# clear all the check boxes
for checkbox in checkboxes:
    if checkbox.is_selected():
        checkbox.click()