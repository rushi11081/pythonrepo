from select import select
from selenium import webdriver
from selenium.webdriver.ie.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service("/Users/Rushikesh Patil/Downloads/chromedriver.exe")

driver = webdriver.Chrome(service=service_obj)

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("rahul")
driver.find_element(By.NAME, "email").send_keys("mystudy@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("Sangola@123")
driver.find_element(By.ID, "exampleCheck1").click()
driver.find_element(By.XPATH, "//input[@class='btn btn-success']").click()

dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(0)
message = driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissible']").text
print(message)

assert "Success" in message

driver.close()
