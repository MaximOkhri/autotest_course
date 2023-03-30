import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/selects2.html")

try:

    first_number = browser.find_element(By.ID, "num1")
    num1 = first_number.text

    second_number = browser.find_element(By.ID, "num2")
    num2 = second_number.text

    sum_num = str(int(num1) + int(num2))

    print(sum_num)

    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(sum_num)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(15)
    browser.quit()