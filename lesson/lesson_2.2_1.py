from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time



link = "http://suninjuly.github.io/selects1.html"

try:  
    browser = webdriver.Chrome()
    browser.get(link)

    # Высчитываем значение для списка
    value = str(int(browser.find_element_by_id("num1").text) + int(browser.find_element_by_id("num2").text))

    # Выбираем знаечние в списке
    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_visible_text(value)
    

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()

