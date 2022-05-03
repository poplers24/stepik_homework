from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/explicit_wait2.html"

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # дожидаемся когда цена цена будет $100
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    btn1 = browser.find_element_by_id("book")
    btn1.click()

    # скрол к окрывшейся части
    browser.execute_script("window.scrollBy(0, 200)")
    
    # высчитываем значение
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    inpFormControl = browser.find_element_by_id("answer")
    inpFormControl.send_keys(y)

    btn2 = browser.find_element_by_id("solve")
    btn2.click()

finally:
    time.sleep(10)
    browser.quit()
