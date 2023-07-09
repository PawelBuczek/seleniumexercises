import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By


def get_element_by(driver: webdriver, by: By, value: str, timeout_in_seconds: int) -> WebElement:
    try:
        return WebDriverWait(driver, timeout=timeout_in_seconds).until(EC.presence_of_element_located((by, value)))
    except:
        print("element with searched:" + value + " was not found! Closing the browser")
        driver.quit()
        quit()


def test_facebook_login():
    driver = webdriver.Chrome()
    driver.get("https://www.facebook.com/")

    get_element_by(driver, By.XPATH, "//button[@title='Decline optional cookies']", 5).click()

    email = get_element_by(driver, By.ID, "email", 1)
    email.click()
    email.clear()
    email.send_keys("myEmail")

    password = get_element_by(driver, By.ID, "pass", 1)
    password.click()
    password.clear()
    password.send_keys("myPassword")

    get_element_by(driver, By.NAME, "login", 1).click()

    mfa = get_element_by(driver, By.ID, "checkpointSubmitButton", 10)
    
    assert mfa.get_property("value") == "continue"

    driver.quit()
