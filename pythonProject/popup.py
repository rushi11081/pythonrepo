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

myname = "rahul"
driver.find_element(By.XPATH,"//input[@id='name']").send_keys(myname)
driver.find_element(By.ID, "alertbtn").click()
alert = driver.switch_to.alert
mytext = alert.text
print(mytext)

assert myname in mytext

alert.accept()