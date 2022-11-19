from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
     
    input1 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Enter first name"]')
    input1.send_keys('name')
    
    input2 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Enter last name"]')
    input2.send_keys('lastname')
    
    input3 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Enter email"]')
    input3.send_keys('name@mail.ru')      
    
    dir_name = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(dir_name, 'file.txt')           # добавляем к этому пути имя файла 
    element = browser.find_element(By.ID, 'file')
    element.send_keys(file_path)    
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()
    
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()