from selenium import webdriver
import time

link = "http://suninjuly.github.io/find_xpath_form"

try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get(link)

    name = browser.find_element_by_tag_name("input").send_keys("Ruslan")
    surname = browser.find_element_by_name(
        "last_name").send_keys("Kirzhanov")
    city = browser.find_element_by_class_name("city").send_keys("Moscow")
    country = browser.find_element_by_id("country").send_keys("Russia")
    button = browser.find_element_by_xpath(
        '/html/body/div[1]/form/div[6]/button[3]').click()

finally:
    time.sleep(5)
    browser.quit()
