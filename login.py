#coding=utf-8

from selenium import webdriver
import time

path="/Users/aimee/Downloads/chromedriver"
driver=webdriver.Chrome(path)

driver.get('https://mail.qq.com')
time.sleep(2)

driver.switch_to.frame('login_frame')
driver.find_element_by_id('u').clear()
driver.find_element_by_id('u').send_keys('1069923094@qq.com')
driver.find_element_by_id('p').clear()
driver.find_element_by_id('p').send_keys('lemon.5941')
driver.find_element_by_id('login_button').click()
time.sleep(3)