# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import config.config

def startBrowser(browser):
    if browser == "chrome":
        service = Service(config.config.chromeDriverExecutePath)
        options = webdriver.ChromeOptions()
        options.add_argument("--incognito")
        
        global driver
        driver = webdriver.Chrome(service=service)
        driver.maximize_window()
    return Browser(driver)

class Browser(object):

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 20
    
    def goToURL(self, url):
        self.driver.get(url)

    def click(self, path, locator=By.XPATH):
        WebDriverWait(self.driver, self.timeout).until(EC.element_to_be_clickable((locator, path))).click()

    def getElement(self, path, locator=By.XPATH):
        element = WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located((locator, path)))
        return element

    def getTitle(self):
        try:
            return self.driver.title
        except:
            return None

    def close(self):
        try:
            self.driver.close()
        except:
            raise("Cannot close browser")

    def screenshot(self, filepath):
        self.driver.save_screenshot(filepath)