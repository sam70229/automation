# -*- coding: utf-8 -*-

from lib.browser import Browser
from config import config


from lib.logger import logger


class Executor(object):

    def execute(function, *args):
        logger.logger.info("Preparing to execute function: %s, with args: %s" % (function.__name__, args))
        try:
            result = function(*args)
            return result
        except:
            Browser().screenshot(config.screenshotFilepath)
