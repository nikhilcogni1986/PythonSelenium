from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

service_obj = Service("E:\\Automation Essentials\\Jars\\106 chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.implicitly_wait(15)
driver.get("https://demo.automationtesting.in/Frames.html")
driver.find_element(By.XPATH, "//a[text()='Iframe with in an Iframe']").click()

outerFrame = driver.find_element(By.XPATH, "//iframe[@src='MultipleFrames.html']")
innerFrame = driver.find_element(By.XPATH, "//iframe[@src='SingleFrame.html']")

driver.switch_to.frame(outerFrame)
driver.switch_to.frame(innerFrame)
driver.find_element(By.XPATH, " //input[@type='text']").send_keys("Text")

