from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://www.google.com/")
time.sleep(2)

print(driver.title)

search = driver.find_element(By.ID, "W0wltc")
search.click()
time.sleep(2)

search = driver.find_element(By.CLASS_NAME, "gLFyf")
search.send_keys("test")
search.send_keys(Keys.RETURN)

time.sleep(5)

driver.quit() # closes entire browser. driver.close() would close only the current tab

