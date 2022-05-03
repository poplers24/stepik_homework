from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/math.html"

try:  
    browser = webdriver.Chrome()
    browser.get(link)
    
    # высчитываем значение
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    
    # заполняем поле
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)
    
    # отмечаем checkbox    
    checkbox = browser.find_element_by_id("robotCheckbox")
    checkbox.click()
    
    # выбираем radio
    radiobutton = browser.find_element_by_id("robotsRule")
    radiobutton.click()

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()

