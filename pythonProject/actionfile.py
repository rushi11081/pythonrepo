import time

from select import select
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.ie.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service("/Users/Rushikesh Patil/Downloads/chromedriver.exe")

driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

action=ActionChains(driver)

action.move_to_element(driver.find_element(By.CSS_SELECTOR,"#mousehover")).perform()
action.move_to_element(driver.find_element(By.LINK_TEXT,"Reload")).click().perform()

action.context_click(driver.find_element(By.XPATH,"//button[text()='Login']")).perform()
