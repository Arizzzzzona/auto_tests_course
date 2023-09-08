from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element(By.XPATH,"//input[@id='answer']")
    input1.send_keys(y)

    checkbox = browser.find_element(By.XPATH,"//input[@id='robotCheckbox']")
    checkbox.click()

    radiobtn = browser.find_element(By.XPATH,"//input[@id='robotsRule']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", radiobtn)
    radiobtn.click()

    btn = browser.find_element(By.XPATH,"//button")
    btn.click()



finally:
    time.sleep(10)
    browser.quit()
    