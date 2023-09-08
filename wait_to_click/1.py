from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    # говорим WebDriver ждать все элементы в течение 5 секунд
    browser.implicitly_wait(5)
    browser.get(link)

    price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID,"price"),"100"))

    btn1 = browser.find_element(By.ID,"book").click() 

    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element(By.XPATH,"//input[@id='answer']")
    input1.send_keys(y)

    btn = browser.find_element(By.ID,"solve")
    browser.execute_script("return arguments[0].scrollIntoView(true);", btn)
    btn.click()


finally:
    time.sleep(10)
    browser.quit()