from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try: 
    link = "http://suninjuly.github.io/file_input.html"

    browser = webdriver.Chrome()
    browser.get(link)
    

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element(By.XPATH,"//input[@name='firstname']")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.XPATH,"//input[@name='lastname']")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.XPATH,"//input[@name='email']")
    input3.send_keys("sss@yandex.ru")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    input4 = browser.find_element(By.XPATH,"//input[@id='file']")
    input4.send_keys(file_path)

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()