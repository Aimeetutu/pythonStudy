# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
import os

path="/Users/aimee/Downloads/chromedriver"
driver = webdriver.Chrome(path)
file_path ='file:///' + os.path.abspath('level_locate.html')
driver.get(file_path)

#点击link1链接（弹出下拉框）
driver.find_element_by_link_text('Link1').click()

#driver.find_element_by_id('dropdown1').is_displayed()

menu=driver.find_element_by_id('dropdown1').find_element_by_link_text('Another action')

#class ActionChains(driver)
#driver: 执行用户操作实例webdriver
#生成用户的行为。所有的行动都存储在actionchains对象。通过perform()存储的行为。
#move_to_element(menu)
#移动鼠标到一个元素中，menu上面已经定义了他所指向的哪一个元素
webdriver.ActionChains(driver).move_to_element(menu).perform()
time.sleep(2)
driver.quit()