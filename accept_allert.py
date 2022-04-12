from selenium import webdriver
import math
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(x))))


link = 'http://suninjuly.github.io/alert_accept.html'

try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get(link)

    magic_button = browser.find_element_by_class_name("btn-primary").click()

    alert = browser.switch_to.alert
    alert.accept()

    x_string = browser.find_element_by_id("input_value")
    x_number = int(x_string.text)

    answer = calc(x_number)

    input_answer = browser.find_element_by_id("answer")
    input_answer.send_keys(answer)

    send_button = browser.find_element_by_class_name("btn-primary")
    send_button.click()

    alert = browser.switch_to.alert
    alert_text = alert.text

    addToClipBoard = alert_text.split(': ')[-1]


finally:
    time.sleep(5)
    browser.quit()
