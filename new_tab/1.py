from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    accept_btn = browser.find_element(By.XPATH,"//button").click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element(By.XPATH,"//input[@id='answer']")
    input1.send_keys(y)

    btn = browser.find_element(By.CSS_SELECTOR,"button.btn").click()





finally:
    time.sleep(10)
    browser.quit()