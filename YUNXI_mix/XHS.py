# android environment
from appium import webdriver
import time


desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '10'
desired_caps['deviceName'] = 'p7ovaidyx85dxsr8'
desired_caps['appPackage'] = 'com.xingin.xhs'
desired_caps['appActivity'] = '.activity.SplashActivity'
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

time.sleep(5)

driver.tap([(562,1345),(922,1459)],500)



time.sleep(5)
driver.tap([(96,1470),(984,1558)], 500)
time.sleep(3)
driver.find_element_by_id("com.xingin.xhs:id/cgv").send_keys("19937158232")
time.sleep(1)
driver.tap([(834,508),(984,549)], 500)


driver.tap(	[(96,604),(124,632)], 500)
time.sleep(1)
a = int(input("...."))
driver.find_element_by_id("com.xingin.xhs:id/a6u").send_keys(a)
time.sleep(1)
driver.tap([(96,740),(984,828)], 500)
time.sleep(100)





