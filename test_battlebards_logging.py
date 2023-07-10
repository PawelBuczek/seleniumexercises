import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
import time


def get_element_by(driver: webdriver, by: By, value: str, timeout_in_seconds: int) -> WebElement:
    try:
        return WebDriverWait(driver, timeout=timeout_in_seconds).until(EC.presence_of_element_located((by, value)))
    except:
        print("element with searched value: '" + value + "' was not found! Closing the browser")
        driver.quit()
        quit()


def test_battlebards_login():
    driver = webdriver.Chrome()
    driver.get("https://battlebards.com/")

    get_element_by(driver, By.XPATH, "//span[text()='Sign In']", 5.0).click()

    email = get_element_by(driver, By.ID, "email", 5.0)
    email.click()
    email.clear()
    email.send_keys("YOUR_EMAIL")

    password = get_element_by(driver, By.ID, "password", 0.5)
    password.click()
    password.clear()
    password.send_keys("YOUR_PASSWORD")

    get_element_by(driver, By.XPATH, "//button[@type='submit' and text()='Sign In']", 0.5).click()

    try:
        WebDriverWait(driver, timeout=4.0).until(EC.presence_of_element_located((By.XPATH, "//button[text()='Continue']"))).click()
    except:
        print("additional confirmation wasn't required this time")

    get_element_by(driver, By.XPATH, "//p[text()='pbuczek']", 7.0)  # just checking that it exists is enough

    time.sleep(4)
    #logging Out - this apparently doesn't work yet
    user_profile = get_element_by(driver, By.XPATH, "//p[@class='header-name' and not(parent::div[@class='user-profile-div']/i)]", 3.0)
    user_profile.click()
    get_element_by(driver, By.XPATH, "//a[@class='signin-text logout-text']", 2.0).click()
    
    time.sleep(3)
    get_element_by(driver, By.XPATH, "//span[text()='Sign In']", 5.0)
    driver.quit()
