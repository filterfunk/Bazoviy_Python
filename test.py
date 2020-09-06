import time

from selenium import webdriver

driver = webdriver.Chrome()
time.sleep(5)

driver.get("https://stepik.org/lesson/25969/step/12")
time.sleep(5)