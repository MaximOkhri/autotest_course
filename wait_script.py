import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

try:
    price_text = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '100'))
    
    price_button = browser.find_element(By.ID, "book")
    price_button.click()


    def calc(text_value):
        return str(math.log(abs(12*math.sin(int(text_value)))))
    formula_text = browser.find_element(By.ID, "input_value")
    text_value = formula_text.text
    answer_value = calc(text_value)

    input_answer = browser.find_element(By.ID, "answer")
    input_answer.send_keys(answer_value)

    button = browser.find_element(By.ID, "solve")
    button.click()

finally:
    time.sleep(15)
    browser.quit()
    