from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/wait1.html")

# пауза, ожидаем появление кнопки
time.sleep(1)

button = browser.find_element_by_id("verify")
button.click()
message = browser.find_element_by_id("verify_message")

# проверяем, что на странице появился ожидаемый текст
assert "successful" in message.text

time.sleep(10)
browser.quit()
