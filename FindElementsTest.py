from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("E:\\Automation Essentials\\Jars\\106 chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("https://demo.nopcommerce.com/register?returnUrl=%2F")
footer_links = driver.find_elements(By.XPATH, "//div[@class='footer']//a")
print(len(footer_links))

for link in footer_links:
    print(link.text)

driver.close()
