from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)


    x_element = browser.find_element(By.XPATH, "//img")
    x = x_element.get_attribute("valuex")
    y = calc(x)
    input1 = browser.find_element(By.XPATH,"//input[@id='answer']")
    input1.send_keys(y)

    checkbox = browser.find_element(By.XPATH,"//input[@id='robotCheckbox']")
    checkbox.click()

    radiobtn = browser.find_element(By.XPATH,"//input[@id='robotsRule']")
    radiobtn.click()

    btn = browser.find_element(By.XPATH,"//button").click()



finally:
    time.sleep(10)
    browser.quit()
    