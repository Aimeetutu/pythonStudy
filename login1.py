#coding=utf-8
from selenium import webdriver
import time

path="/Users/aimee/Downloads/chromedriver"
driver=webdriver.Chrome(path)
driver.get("https://mail.163.com/")
time.sleep(2)
driver.switch_to.frame("x-URS-iframe")
driver.find_element_by_name('email').clear()
driver.find_element_by_name('email').send_keys("aimee_tu1@163.com")
driver.find_element_by_name('password').clear()
driver.find_element_by_name('password').send_keys("x3141y")
time.sleep(1)
driver.find_element_by_id("dologin").click()
time.sleep(5)
# driver.close()

cookie=driver.get_cookie(value)
print(cookie)


# driver.add_cookie({'name':'aimee_tu1@163.com','value':'x3141y'})
# for cookie in driver.get_cookies():
#     print cookie['name'],cookie['value']






# driver.switch_to.frame("login_frame")
# driver.find_element_by_id('switcher_plogin').click()
# driver.find_element_by_id('u').clear()
# driver.find_element_by_id('u').send_keys('10699230942qq.com')
# driver.find_element_by_id('p').clear()
# driver.find_element_by_id('p').send_keys('lemon.5941')
# driver.find_element_by_id('login_button').click()
driver.close()
# driver.add_cookie({'name':'key-aaaa','value':'value-bbbb'})
# for cookie in driver.get_cookies():
#     print('%s -> %s' % (cookie['name'],cookie['value']))
# driver.quit()
