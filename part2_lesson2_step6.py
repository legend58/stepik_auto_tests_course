from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    # Ваш код, который заполняет обязательные поля
    x = int(browser.find_element(By.ID, 'input_value').text)
    y = calc(x)
        
    # Отправляем заполненную форму
    
    input2 = browser.find_element(By.CSS_SELECTOR, '#answer')
    browser.execute_script("return arguments[0].scrollIntoView(true);", input2)
    input2.send_keys(y)
    
    option1 = browser.find_element(By.ID, "robotCheckbox")
    option1.click()    
    
    option2 = browser.find_element(By.ID, "robotsRule")
    option2.click()        
    
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()
    
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()