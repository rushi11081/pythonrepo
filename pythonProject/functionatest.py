import time

from select import select
from selenium import webdriver
from selenium.webdriver.ie.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service("/Users/Rushikesh Patil/Downloads/chromedriver.exe")
expectedlist = ['Cucumber - 1 Kg', 'Raspberry - 1/4 Kg', 'Strawberry - 1/4 Kg']

actuallist = []
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(2)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(4)

results = driver.find_elements(By.XPATH, "//div[@class='products']/div")  # list[]
count = len(results)
assert count > 0
for result in results:
    result.find_element(By.XPATH, "div/button").click()
    actuallist.append(result.find_element(By.XPATH,"h4").text)
driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()  # 15
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

assert actuallist == expectedlist

# Sum validation
prices = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(5) p")
sum = 0
for price in prices:
    sum = sum + int(price.text)

print(sum)
totalAmount = int(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)

assert sum == totalAmount


driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))
print(driver.find_element(By.CLASS_NAME, "promoInfo").text)

dm=float(driver.find_element(By.CSS_SELECTOR,".discountAmt").text)

assert totalAmount > dm