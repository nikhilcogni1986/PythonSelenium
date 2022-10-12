from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service_obj = Service("E:\\Automation Essentials\\Jars\\106 chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.implicitly_wait(15)
driver.get("https://demo.nopcommerce.com/register?returnUrl=%2F")
driver.maximize_window()

# get the source of page
print(driver.page_source)

# get current url of the window opened
print(driver.current_url)

# close the focused window of the browser
driver.close()