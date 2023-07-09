from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
import re


def getElementById(driver: webdriver, id: str, timeout_in_seconds: int) -> WebElement:
    try:
        return WebDriverWait(driver, timeout=timeout_in_seconds).until(EC.presence_of_element_located((By.ID, id)))
    except:
        print("element with id:" + id + " was not found! Closing the browser")
        driver.quit()
        quit()


if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.get("https://orteil.dashnet.org/experiments/cookie/")

    cookie = getElementById(driver, "cookie", 5.0)
    money = getElementById(driver, "money", 1.0)
    buyCursor = getElementById(driver, "buyCursor", 1.0)
    buyGrandma = getElementById(driver, "buyGrandma", 1.0)

    for i in range(10000):
        try:
            cookie.click()
            print("we have " + money.text + " cookies")
            print("next cursor costs " + re.findall('\d+', buyCursor.text)[0] + " cookies")
            print("next grandma costs " + re.findall('\d+', buyGrandma.text)[0] + " grandma")

            if (int(money.text) >= int(re.findall('\d+', buyGrandma.text)[0])):
                buyGrandma.click()
            if (int(money.text) >= int(re.findall('\d+', buyCursor.text)[0])):
                buyCursor.click()
        except:
            cookie = getElementById(driver, "cookie", 1.0)
            money = getElementById(driver, "money", 1.0)
            buyCursor = getElementById(driver, "buyCursor", 1.0)
            buyGrandma = getElementById(driver, "buyGrandma", 1.0)

    driver.quit()  # closes entire browser. driver.close() would close only the current tab
