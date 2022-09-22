from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

link = "https://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)
    y_element = browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(y)
    option1 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    option1.click()
    option2 = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    option2.click()
    option3 = browser.find_element(By.CSS_SELECTOR, ".btn-default")
    option3.click()
finally:
    time.sleep(5)
    browser.quit()