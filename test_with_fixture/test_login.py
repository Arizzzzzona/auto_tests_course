import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def calc(x):
    return str(math.log(int(time.time())))

#link = "https://stepik.org/lesson/236895/step/1"



@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('id', ["236895","236896","236897","236898","236899","236903","236904","236905"])
def test_login_link(browser,id):
    link = f"https://stepik.org/lesson/{id}/step/1"
    browser.get(link)
    browser.implicitly_wait(10)
    btn = browser.find_element(By.XPATH, "//*[@class='ember-view navbar__auth navbar__auth_login st-link st-link_style_button']")
    btn.click()
    
    input1 = browser.find_element(By.NAME,"login")
    input1.send_keys("mail")

    inpu2 = browser.find_element(By.NAME,"password")
    inpu2.send_keys("pass")


    element1 = WebDriverWait(browser,10).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='login_form']/button")))
    browser.find_element(By.XPATH,"//*[@id='login_form']/button").click()

    time.sleep(10)
    
    answer = calc(time)

    input3 = browser.find_element(By.XPATH,"//textarea")
    input3.send_keys(answer)

    #element = WebDriverWait(browser,10).until(EC.element_to_be_clickable((By.XPATH,"//*[@class='submit-submission']")))
    btn2 = browser.find_element(By.XPATH,"//*[contains(@class,'submit-submission')]")
    btn2.click()

    browser.implicitly_wait(10)
    text_msg = browser.find_element(By.XPATH,"//*[@class='smart-hints ember-view lesson__hint']/p")

    res = text_msg.text

    assert "Correct!" == res




