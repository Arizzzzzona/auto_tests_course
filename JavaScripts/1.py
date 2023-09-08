from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)

    btn = browser.find_element(By.XPATH,"//button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", btn)
    btn.click()

finally:
    time.sleep(10)