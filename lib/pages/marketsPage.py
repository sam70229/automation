# -*- coding: utf-8 -*-

from lib.pages import basePage

class MarketsPage(basePage.BasePage):

    locators = {
        "usdc_tab": "//div[@class='e-tabs__nav-item'][text()='USDC']",
        "trade_btn": "//*[@class='base'][text()='coin_name_to_replace']/ancestor::tr//td[last()]//*[text()='Trade']"
    }

    def switch_to_usdc_tab(self):
        self.driver.click(self.locators["usdc_tab"])

    def click_trade_button(self, coin_name):
        xpath = self.locators["trade_btn"]
        new_xpath = xpath.replace("coin_name_to_replace", coin_name)
        self.driver.click(new_xpath)