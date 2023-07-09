from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://orteil.dashnet.org/experiments/cookie/")


driver.quit() # closes entire browser. driver.close() would close only the current tab

