from selenium import webdriver
import time

browser = webdriver.Chrome()

# говорим WebDriver искать каждый элемент в течение 5 секунд
browser.implicitly_wait(5)

browser.get("http://suninjuly.github.io/wait1.html")

button = browser.find_element_by_id("verify")
button.click()
message = browser.find_element_by_id("verify_message")


# проверяем, что на странице появился ожидаемый текст
assert "successful" in message.text

time.sleep(10)
browser.quit()
