import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x = browser.find_element(By.ID, 'input_value').text
    d = str(math.log(abs(12*math.sin(int(x)))))
    browser.find_element(By.ID, 'answer').send_keys(d)
    browser.find_element(By.ID, 'robotCheckbox').click()
    check = browser.find_element(By.ID, "robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", check)
    check.click()
    time.sleep(1)
    browser.find_element(By.CLASS_NAME, "btn-primary").click()
finally:
    time.sleep(10)
    browser.quit()