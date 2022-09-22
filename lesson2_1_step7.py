from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    treasure = browser.find_element(By.ID, "treasure")
    treasure_value = treasure.get_attribute("valuex")
    x = treasure_value
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
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