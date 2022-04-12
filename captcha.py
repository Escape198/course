from selenium import webdriver

import math
import time


link = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    x_in_first_test = browser.find_element_by_id("input_value")
    x_value = x_in_first_test.text

    first_test_result = calc(x_value)

    first_test_input = browser.find_element_by_id("answer")
    first_test_input.send_keys(first_test_result)
    robot_checkbox = browser.find_element_by_id("robotCheckbox").click()
    robot_radiobutton = browser.find_element_by_id("robotsRule").click()
    send_button = browser.find_element_by_class_name("btn-default").click()

finally:
    time.sleep(4)
    browser.quit()
