from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service("E:\\Automation Essentials\\Jars\\106 chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.implicitly_wait(15)
driver.get("https://itera-qa.azurewebsites.net/home/automation")
driver.maximize_window()

dropdown = driver.find_element(By.XPATH, "//select[@class='custom-select']")
s1 = Select(dropdown)
s1.select_by_index(2)
s1.select_by_value("10")
s1.select_by_visible_text("Norway")

allOptions = s1.options
for option in allOptions:
    if option.text == 'Greece':
        option.click()
    print(option.text)