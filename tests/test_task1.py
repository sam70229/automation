# -*- coding: utf-8 -*-
import sys
sys.path.append(".")

from lib.pages.exchangePage import ExchangePage
from lib.pages.marketsPage import MarketsPage
from lib.pages.tradePage import TradePage
from lib.browser import *
from lib.utility import Executor


def setup_function():
    global driver
    driver = startBrowser("chrome")
    driver.goToURL("https://crypto.com/exchange")
    
def test_task1():
    
    #Go to markets page
    exchange_page = ExchangePage(driver)
    exchange_page.clickMarketsTab()

    #Switch to usdc tab and click trade button on CRO row
    markets_page = MarketsPage(driver)
    markets_page.switch_to_usdc_tab()
    markets_page.click_trade_button("CRO")

    #Check is in trade page of CRO
    trade_page = TradePage(driver)
    assert trade_page.is_in_correct_trade_page("CRO/USDC")

def teardown_function():
    driver.close()
