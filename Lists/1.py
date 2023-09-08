from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

def calc(sum):
    return str(int(x) + int(y))

try:
    link = "https://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element(By.XPATH,"//*[@id='num1']")
    x = num1.text

    num2 = browser.find_element(By.XPATH,"//*[@id='num2']")
    y = num2.text

    res = calc(sum)
    
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_visible_text(res)

    btn = browser.find_element(By.XPATH,"//button").click()

finally:
    time.sleep(10)
    browser.quit()
    
