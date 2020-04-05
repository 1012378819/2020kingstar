import configparser
import os.path
from selenium import webdriver
from framework.logger import Logger

logger=Logger(logger="BrowserEngine").getlog()

class BrowserEngine():
    dir=os.path.dirname(os.path.abspath('.'))
    chrome_driver_path=dir+'/tools/chromedriver.exe'
    ie_driver_path=dir+'/tools/IEDriverServer.exe'

    def __init__(self,driver):
        self.driver=driver

    def open_browser(self,driver):
        config=configparser.ConfigParser()
        file_path=os.path.dirname(os.path.abspath('.'))+'/config/config.ini'
        config.read(file_path)

        browser=config.get('browserType','browserName')
        logger.info('you had select %s browser.'% browser)
        url=config.get('testServer','url')
        logger.info('The test server url is:%s ' %url)

        if browser=='Firefox':
            driver=webdriver.Firefox()
            logger.info("Starting firefox browser.")
        elif browser=='Chrome':
            driver=webdriver.Chrome(self.chrome_driver_path)
            logger.info("Staring Chrome browser.")
        elif browser=='IE':
            driver=webdriver.Ie(self.ie_driver_path)
            logger.info('starting IE browser.')

        driver.get(url)
        logger.info('Open url:%s' %url)
        driver.maxmize_window()
        logger.info("Maximize the current window.")
        driver.implicitly_wait(5)
        logger.info("Set implicitly wait 5 secends.")
        return driver

    def quit_browser(self):
        logger.info("Now,Close and quit the browser.")
        self.driver.quit()
