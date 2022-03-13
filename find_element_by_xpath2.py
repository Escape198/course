

from selenium import webdriver
import time


link = "http://suninjuly.github.io/registration1.html"
browser = webdriver.Chrome()
browser.implicitly_wait(5)


try:
    browser.get(link)

    name = browser.find_element_by_xpath(
        '/html/body/div[1]/form/div[1]/div[1]/input').send_keys("Ruslan")
    surname = browser.find_element_by_xpath(
        '/html/body/div[1]/form/div[1]/div[2]/input').send_keys("Kirzhanov")
    email = browser.find_element_by_xpath(
        '/html/body/div[1]/form/div[1]/div[3]/input').send_keys("r.kirzhanov@albato.ru")

    button = browser.find_element_by_css_selector("button.btn").click()

    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text, 'Что-то пошло не так.'


finally:
    time.sleep(2)
    browser.quit()
