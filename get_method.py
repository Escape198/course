

import time
from selenium import webdriver


driver = webdriver.Chrome()
browser.implicitly_wait(5)


try:
    driver.get("https://stepik.org/lesson/25969/step/12")

    textarea = driver.find_element_by_css_selector(".textarea")
    textarea.send_keys("get()")

    submit_button = driver.find_element_by_css_selector(
        ".submit-submission").click()


finally:
    time.sleep(5)
    driver.quit()
