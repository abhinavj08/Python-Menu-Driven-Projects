from selenium import webdriver
import time

driver = webdriver.Edge()

driver.get("https://www.google.com")

time.sleep(5)

driver.quit()