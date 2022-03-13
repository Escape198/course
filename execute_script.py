

from selenium import webdriver
import math
import time


link = "http://SunInJuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.implicitly_wait(5)
browser.get(link)


try:
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x_in_text = browser.find_element_by_id("input_value")
    x_value = x_in_text.text

    first_answer = calc(x_value)

    first_input = browser.find_element_by_id("answer")
    browser.execute_script(
        "return arguments[0].scrollIntoView(true);", first_input)

    first_input.send_keys(first_answer)

    robotCheckbox = browser.find_element_by_id("robotCheckbox")
    robotCheckbox.click()

    robotRadiobutton = browser.find_element_by_id("robotsRule")
    robotRadiobutton.click()

    send_button = browser.find_element_by_xpath(
        '/html/body/div[1]/form/button')
    send_button.click()


finally:
    time.sleep(3)
    browser.quit
