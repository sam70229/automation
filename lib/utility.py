# -*- coding: utf-8 -*-
import json

from lib.logger import logger
from lib.browser import Browser
from lib.variable import *
from config import config


class Executor(object):

    def execute(function, *args):
        logger.logger.info("Preparing to execute function: %s, with args: %s" % (function.__name__, args))
        print("Prepare to run %s..." % (function.__name__))
        try:
            result = function(*args)
            return result
        except:
            logger.logger.info("Failed to execute function: %s, with args: %s" % (function.__name__, args))


class DataLoader(object):

    def loadJsonXpath(self):
        with open(config.jsonDataPath) as f:
            jsonXpath = json.loads(f.read())
