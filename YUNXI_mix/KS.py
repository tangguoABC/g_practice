# android environment
from appium import webdriver
import time


desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '10'
desired_caps['deviceName'] = 'fecde1fb'
desired_caps['appPackage'] = 'com.smile.gifmaker'
desired_caps['appActivity'] = 'com.yxcorp.gifshow.HomeActivity'
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

time.sleep(5)
driver.find_element_by_id('com.smile.gifmaker:id/positive').click()

time.sleep(5)
driver.quit()