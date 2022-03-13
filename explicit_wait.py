from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from math import log, sin
import time

browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/explicit_wait2.html'

try:
    browser.get(link)

    WebDriverWait(browser, 13).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))

    browser.find_element_by_id('book').click()

    browser.find_element_by_id('answer').send_keys(
        str(log(abs(12 * sin(int(browser.find_element_by_id('input_value').text)))))
    )
    browser.find_element_by_id('solve').click()

    alert = browser.switch_to.alert
    alert_text = alert.text
    addToClipBoard = alert_text.split(': ')[-1]


finally:
    time.sleep(3)
    browser.quit()
