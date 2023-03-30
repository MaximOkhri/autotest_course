from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    driver = webdriver.Chrome()
    driver.get("http://suninjuly.github.io/simple_form_find_task.html")
    button = driver.find_element(By.ID, "submit_button")
    button.click()
    
finally:
    driver.quit()