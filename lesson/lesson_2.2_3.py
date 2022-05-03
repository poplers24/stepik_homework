from selenium import webdriver
import time
import os


link = "http://suninjuly.github.io/file_input.html"

try:  
    browser = webdriver.Chrome()
    browser.get(link)

    # заполняем поля
    inpFirstName = browser.find_element_by_name("firstname")
    inpFirstName.send_keys("Ivan")
    inpLastName = browser.find_element_by_name("lastname")
    inpLastName.send_keys("Petrov")
    inpEmail = browser.find_element_by_name("email")
    inpEmail.send_keys("test@test.ru")

    # загружаем файл
    file_element = browser.find_element_by_id("file")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, "file.txt")
    file_element.send_keys(file_path)

    # отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()

