import time

from select import select
from selenium import webdriver
from selenium.webdriver.ie.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service("/Users/Rushikesh Patil/Downloads/chromedriver.exe")

driver = webdriver.Chrome(service=service_obj)

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.ID, "autocomplete").send_keys("ind")
time.sleep(2)
countries = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] ")
print(len(countries))
for country in countries:
    if country.text == "India":
        country.click()
        break
print(driver.find_element(By.ID, "autocomplete").get_attribute("value"))

assert driver.find_element(By.ID, "autocomplete").get_attribute("value") == "India"

radiobutton = driver.find_elements(By.CSS_SELECTOR, ".radioButton")
time.sleep(2)
radiobutton[2].click()
assert radiobutton[2].is_selected()

