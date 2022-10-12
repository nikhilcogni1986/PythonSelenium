import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("E:\\Automation Essentials\\Jars\\106 chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.implicitly_wait(15)
driver.get("http://www.deadlinkcity.com/")
driver.maximize_window()

count = 0
allLinks = driver.find_elements(By.TAG_NAME, "a")
print(allLinks)

for link in allLinks:
    url = link.get_attribute('href')
    try:
        response = requests.head(url)
    except:
        None
    if response.status_code >= 400:
        print(url + " Its a broken link")
        count = count + 1
    else:
        print(url + "is a valid link")
print("Number of broken links are: ", count)
