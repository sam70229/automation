# -*- coding: utf-8 -*-
from lib.pages import basePage
from lib.logger.logger import *


class ExchangePage(basePage.BasePage):

    locators = {"markets": "//button[@type='button'][text()='Markets']"}

    def clickMarketsTab(self):
        logger.info("path: %s" % (self.locators["markets"]))
        self.driver.click(self.locators["markets"])

    def is_title_match(self):
        return self.driver.getTitle() == "Crypto.com Exchange"
