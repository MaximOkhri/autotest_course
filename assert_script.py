import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/registration1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.XPATH, "//input[@placeholder='Input your first name']")
    input1.send_keys("Dr.")
    time.sleep(3)
    input2 = browser.find_element(By.XPATH, "//input[@placeholder='Input your last name']")
    input2.send_keys("Akula")
    time.sleep(3)
    input3 = browser.find_element(By.XPATH, "//input[@placeholder='Input your email']")
    input3.send_keys("Dr.Akula@gmail.com")
    time.sleep(3)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    

    time.sleep(1)

    welcome_text_elem = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elem.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()