#coding=utf-8
from selenium import webdriver
import time
import os

path="/Users/aimee/Downloads/chromedriver"
driver = webdriver.Chrome(path)
file_path='file:///'+os.path.abspath('checkbox.html')
driver.get(file_path)

checkboxs=driver.find_elements_by_css_selector('input[type=checkbox]')
for check in checkboxs:
    check.click()

time.sleep(1)

driver.find_elements_by_css_selector('input[type=checkbox]').pop(1).click()
time.sleep(2)

driver.quit()