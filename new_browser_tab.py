

from selenium import webdriver
import math
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(x))))


link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.implicitly_wait(5)


try:
    browser.get(link)

    button = browser.find_element_by_class_name("btn-primary")
    button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x_string = browser.find_element_by_id("input_value")
    x_number = int(x_string.text)

    answer = calc(x_number)

    input_answer = browser.find_element_by_id("answer")
    input_answer.send_keys(answer)

    send_button = browser.find_element_by_class_name("btn-primary")
    send_button.click()

    alert = browser.swith_to.alert
    alert_text = alert.text

    addToClipboard = alert_text.split(": ")[-1]
    pyperclip.copy(addToClipboard)


finally:
    time.sleep(3)
    browser.quit()
