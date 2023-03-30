import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/execute_script.html")

try:
    
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    formula_text = browser.find_element(By.ID, "input_value")
    x = formula_text.text
    y = calc(x)

    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)

    checkbox1 = browser.find_element(By.ID, "robotCheckbox")
    checkbox1.click()

    browser.execute_script("window.scrollBy(0, 100);")

    radiobutton1 = browser.find_element(By.ID, "robotsRule")
    radiobutton1.click()

    button1 = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button1.click()

finally:

    time.sleep(15)
    browser.quit()