import time

from select import select
from selenium import webdriver
from selenium.webdriver.ie.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service("/Users/Rushikesh Patil/Downloads/chromedriver.exe")
product = []
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(2)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()
elementlist = driver.find_elements(By.XPATH, "//tr/td[1]")

for ele in elementlist:
    product.append(ele.text)

original = product.copy()
product.sort()

assert product == original
