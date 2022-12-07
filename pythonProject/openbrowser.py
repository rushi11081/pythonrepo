from selenium import webdriver
from selenium.webdriver.ie.service import Service

service_obj = Service("/Users/Rushikesh Patil/Downloads/chromedriver.exe")

driver = webdriver.Chrome(service=service_obj)

driver.maximize_window()
driver.get("https://rahulshettyacademy.com")
print(driver.title)
print(driver.current_url)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
print(driver.current_url)
driver.minimize_window()
driver.back()
driver.refresh()
driver.forward()
driver.close()