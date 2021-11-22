# -*- coding: utf-8 -*-
import sys
sys.path.append(".")

from lib.pages import exchangePage, marketsPage, tradePage
from lib import browser
from lib.utility import Executor


def setup_function():
    global driver
    driver = browser.startBrowser("chrome")
    driver.goToURL("https://crypto.com/exchange")
    
def test_task1():
    #Load exchange page
    exchange_page = Executor.execute(exchangePage.ExchangePage, driver)
    assert exchange_page.is_title_match()

    #Go to markets page
    Executor.execute(exchange_page.clickMarketsTab)

    #Switch to usdc tab and click trade button on CRO row
    markets_page = Executor.execute(marketsPage.MarketsPage, driver)
    Executor.execute(markets_page.switch_to_usdc_tab)
    Executor.execute(markets_page.click_trade_button, "CRO")

    #Check is in trade page of CRO
    trade_page = Executor.execute(tradePage.TradePage, driver)
    assert trade_page.is_in_correct_trade_page("CRO/USDC")

def teardown_function():
    driver.close()
