from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"

try:  
    browser = webdriver.Chrome()
    browser.get(link)

    btn1 = browser.find_element_by_css_selector(".trollface.btn")
    btn1.click()

    # переключаемся на вторую вкладку
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    
    # высчитываем значение
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    
    # заполняем поле
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)

    btn2 = browser.find_element_by_css_selector("button.btn")
    btn2.click()

finally:
    time.sleep(10)
    browser.quit()

