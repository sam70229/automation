# -*- coding: utf-8 -*-
from pathlib import Path

from lib.browser import Browser
from lib import variable
from lib.logger import logger
from lib.pages import basePage


class TradePage(basePage.BasePage):

    locators = {
        "panel_title": "//*[@class='toggle'][normalize-space(text())='coin_name_to_replace']"
    }
    
    def is_in_correct_trade_page(self, coin_name):
        xpath = self.locators["panel_title"]
        new_xpath = xpath.replace("coin_name_to_replace", coin_name)
        logger.logger.info("Checking xpath: %s" % (new_xpath))
        return self.driver.getElement(new_xpath) is not None
