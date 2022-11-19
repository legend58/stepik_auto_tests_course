from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
     
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()
    
    alert = browser.switch_to.alert
    alert.accept()
    
    time.sleep(1)
    input1 = browser.find_element(By.ID, 'input_value')
    x = int(input1.text)
    result = calc(x)
    input2 = browser.find_element(By.CSS_SELECTOR, '#answer')
    input2.send_keys(result)   
    
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()    
    
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()