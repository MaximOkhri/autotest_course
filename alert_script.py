import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/alert_accept.html")

try:
    main_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    main_button.click()

    conf_window = browser.switch_to.alert
    conf_window.accept()

    def calc(text_value):
        return str(math.log(abs(12*math.sin(int(text_value)))))
    formula_text = browser.find_element(By.ID, "input_value")
    text_value = formula_text.text
    answer_value = calc(text_value)

    input_answer = browser.find_element(By.ID, "answer")
    input_answer.send_keys(answer_value)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(15)
    browser.quit()