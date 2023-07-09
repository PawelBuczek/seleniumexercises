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
        print("element with searched value:" + value + " was not found! Closing the browser")
        driver.quit()
        quit()


def test_facebook_login():
    driver = webdriver.Chrome()
    driver.get("https://www.youtube.com/")

    get_element_by(driver, By.XPATH, "//span[text()='Reject all']/ancestor::button", 7.0).click()

    get_element_by(driver, By.XPATH, "(//a[@aria-label='Sign in'])[1]", 2.0).click() 

    email = get_element_by(driver, By.ID, "identifierId", 5.0)
    email.click()
    email.clear()
    email.send_keys("warsong93@gmail.com")

    get_element_by(driver, By.XPATH, "//span[text()='Next']/ancestor::button", 1.0).click()

    pytest.set_trace()

    # and here it breaks, ah, great gods, youtube, it's so bad
    
    driver.quit()
