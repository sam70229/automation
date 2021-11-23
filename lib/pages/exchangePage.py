# -*- coding: utf-8 -*-
from pathlib import Path

from lib.browser import Browser
from lib import variable
from lib.logger import logger
from lib.pages import basePage


class ExchangePage(basePage.BasePage):

    locators = {
        "markets": "//button[@type='button'][text()='Markets']"
    }

    def clickMarketsTab(self):
        xpath = self.locators["markets"]
        logger.logger.info("%s, %s" % (Path(__file__).stem, xpath))
        logger.logger.info("path: %s" % (xpath))
        self.driver.click(xpath)

    def is_title_match(self):
        return self.driver.getTitle() == "Crypto.com Exchange"
