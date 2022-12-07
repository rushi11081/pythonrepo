import time

from select import select
from selenium import webdriver
from selenium.webdriver.ie.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service("/Users/Rushikesh Patil/Downloads/chromedriver.exe")

driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(2)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(2)
results = driver.find_elements(By.XPATH, "//div[@class='products']/div")

count = len(results)

print(count)
assert count > 0

# //button[text()='ADD TO CART']
for result in results:
    result.find_element(By.XPATH, "div/button").click()

    driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()

driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
driver.find_element(By.CLASS_NAME, "promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()

# wait = WebDriverWait(driver, 10)
# wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,".promoInfo")))
# print(driver.find_element(By.CLASS_NAME, "promoInfo").text())

amt = driver.find_element(By.XPATH, "//tr[1]/td[5]/p").text

at = int(amt)

total = driver.find_element(By.XPATH, "//span[@class='totAmt']").text

tm = int(total)

assert at == tm
