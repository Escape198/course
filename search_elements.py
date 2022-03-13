

from selenium import webdriver
import time

link = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get(link)

    input1 = browser.find_element_by_tag_name("input")
    input1.send_keys("Ruslan")
    input2 = browser.find_element_by_name("last_name")
    input2.send_keys("Kirzhanov")
    input3 = browser.find_element_by_class_name("city")
    input3.send_keys("Moscow")
    input4 = browser.find_element_by_id("country")
    input4.send_keys("Russia")
    button = browser.find_element_by_css_selector("button.btn").click()

finally:
    time.sleep(3)
    browser.quit()

