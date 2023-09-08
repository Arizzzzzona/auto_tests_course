import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class TestForm(unittest.TestCase):
    

    def test_form1(self):
        try:
            link = "http://suninjuly.github.io/registration1.html"
            browser = webdriver.Chrome()
            browser.get(link)
            
            # Код, который заполняет обязательные поля
            input1 = browser.find_element(By.XPATH,"//div[contains(@class,'first_block')]//input[contains(@class,'form-control first')]")
            input1.send_keys("Ivan")
            input2 = browser.find_element(By.XPATH,"//div[contains(@class,'first_block')]//input[contains(@class,'form-control second')]")
            input2.send_keys("Petrov")
            input3 = browser.find_element(By.XPATH,"//div[contains(@class,'first_block')]//input[contains(@class,'form-control third')]")
            input3.send_keys("sss@yandex.ru")

             # Отправляем заполненную форму
            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()

            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
            time.sleep(1)

            # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text
            text = "Congratulations! You have successfully registered!"

            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            self.assertEqual(welcome_text, text, "Oops!" )
            
        finally:
            browser.quit()
        

    def test_form2(self):
        try:
            link = "http://suninjuly.github.io/registration2.html"
            browser = webdriver.Chrome()
            browser.get(link)
            
            # Код, который заполняет обязательные поля
            input1 = browser.find_element(By.XPATH,"//div[contains(@class,'first_block')]//input[contains(@class,'form-control first')]")
            input1.send_keys("Ivan")
            input2 = browser.find_element(By.XPATH,"//div[contains(@class,'first_block')]//input[contains(@class,'form-control second')]")
            input2.send_keys("Petrov")
            input3 = browser.find_element(By.XPATH,"//div[contains(@class,'first_block')]//input[contains(@class,'form-control third')]")
            input3.send_keys("sss@yandex.ru")

             # Отправляем заполненную форму
            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()

            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
            time.sleep(1)

            # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text
            text = "Congratulations! You have successfully registered!"

            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            self.assertEqual(welcome_text, text, "Oops!" )
            
        finally:
            browser.quit()
        
        
if __name__ == "__main__":
    unittest.main()