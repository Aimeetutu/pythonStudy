
from appium import webdriver


desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '7.0'
desired_caps['deviceName'] = 'SLA-AL00'
desired_caps['appPackage'] = 'com.taobao.taobao'
desired_caps['appActivity'] = 'com.taobao.tao.welcome.Welcome'

#desired_caps['app'] = os.path.abspath('/Users/aimee/Downloads/sample-code-master/sample-code/apps/ApiDemos/bin/ApiDemos-debug.apk')

wd = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

http://blog.chinaunix.net/uid-29381304-id-5691193.html

http://ask.csdn.net/questions/362244