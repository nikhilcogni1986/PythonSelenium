from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service("E:\\Automation Essentials\\Jars\\106 chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://chercher.tech/practice/explicit-wait-sample-selenium-webdriver")
driver.implicitly_wait(5)
driver.maximize_window()

driver.find_element(By.ID, "display-other-button").click()
mywait = WebDriverWait(driver, 15)
enabled_button = driver.find_element(By.XPATH, "//button[@id='hidden']")
mywait.until(EC.visibility_of(enabled_button))
print(enabled_button.text)

driver.find_element(By.ID, "enable-button").click()
btn_enabled = driver.find_element(By.ID, "disable")
btn_enabled = mywait.until(EC.element_to_be_clickable(btn_enabled))
btn_enabled.click()


driver.close()