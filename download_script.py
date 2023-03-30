import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/file_input.html")

try:
    first_name = browser.find_element(By.NAME, "firstname")
    first_name.send_keys("Dr.")

    last_name = browser.find_element(By.NAME, "lastname")
    last_name.send_keys("Akula")

    email_name = browser.find_element(By.NAME, "email")
    email_name.send_keys("Dr.Akula@gmail.com")

    download_file = browser.find_element(By.ID, "file")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, "file.txt")
    download_file.send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(15)
    browser.quit()