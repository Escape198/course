

from selenium import webdriver
import math
import time


link = "http://suninjuly.github.io/find_link_text"
browser = webdriver.Chrome()
browser.implicitly_wait(5)


try:
    browser.get(link)

    link_number = str(math.ceil(math.pow(math.pi, math.e) * 10000))
    needed_link = browser.find_element_by_link_text(link_number).click()

    name = browser.find_element_by_tag_name("input").send_keys("Ruslan")
    surname = browser.find_element_by_name(
        "last_name").send_keys("Kirzhanov")
    city = browser.find_element_by_class_name("city").send_keys("Moscow")
    country = browser.find_element_by_id("country").send_keys("Russia")
    button = browser.find_element_by_css_selector("button.btn").click()


finally:
    time.sleep(3)
    browser.quit()
