from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://www.google.com/")
time.sleep(2)

print(driver.title)

search = driver.find_element(By.ID, "W0wltc")
search.click()

WebDriverWait(driver, timeout=10).until(EC.presence_of_element_located((By.CLASS_NAME, "gLFyf")))
search = driver.find_element(By.CLASS_NAME, "gLFyf")
time.sleep(1)
search.send_keys("test")
time.sleep(1)
search.send_keys(Keys.ESCAPE)
time.sleep(1)
search.send_keys(Keys.RETURN)

time.sleep(4)

driver.quit() # closes entire browser. driver.close() would close only the current tab

