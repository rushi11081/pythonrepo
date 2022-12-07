import time

from select import select
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.ie.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service("/Users/Rushikesh Patil/Downloads/chromedriver.exe")

driver = webdriver.Chrome(service=service_obj)
# driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/windows")
# time.sleep(3)
driver.find_element(By.LINK_TEXT, "Click Here").click()
# time.sleep(2)
newwind = driver.window_handles

driver.switch_to.window(newwind[1])
print(driver.find_element(By.TAG_NAME, "h3").text)

driver.switch_to.window(newwind[0])
print(driver.find_element(By.TAG_NAME, "h3").text)

assert "Opening a new window" == driver.find_element(By.TAG_NAME, "h3").text
