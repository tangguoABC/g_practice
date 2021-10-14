# -*- coding:utf-8 -*-
import configparser
import os
from selenium import webdriver
from Automation_demo.framework.logger import Logger

logger = Logger(logger="BrowserEngine").getlog()


class BrowserEngine(object):

    def __init__(self, driver):
        self.driver = driver

    def open_browser(self, driver):
        config = configparser.ConfigParser()
        file_path = os.path.dirname(os.path.abspath('.')) + '\config\config.ini'
        config.read(file_path,encoding='UTF-8')

        browser = config.get("browserType", "browserName")
        logger.info("你选择了浏览器： %s" % browser)
        url = config.get("testServer", "URL")
        logger.info("你选择的网页: %s" % url)

        if browser == "Firefox":
            self.driver = webdriver.Firefox()
            logger.info("启动浏览器.")
        elif browser == "Chrome":
            driver = webdriver.Chrome()
            logger.info("Starting Chrome browser.")
        elif browser == "IE":
            driver = webdriver.Ie()
            logger.info("Starting IE browser.")

        driver.get(url)
        logger.info("Open url: %s" % url)
        driver.maximize_window()
        logger.info("Maximize the current window.")
        driver.implicitly_wait(10)
        logger.info("Set implicitly wait 10 seconds.")
        return driver

    def quit_browser(self):
        logger.info("Now, Close and quit the browser.")
        self.driver.quit()










