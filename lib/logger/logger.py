# -*- coding: utf-8 -*-
import logging.config
import os
import sys

from config import config
from lib import variable


class TerminalOutput(object):

    def __init__(self):
        self.console = sys.stdout
        if os.path.exists(config.consoleLogFile):
            self.log = open(config.consoleLogFile, "a")
        else:
            self.log = open(config.consoleLogFile, "w")

    def __del__(self):
        if self.log:
            self.log.close()
    
    def flush(self):
        pass

    def isatty(self):
        return True

    def write(self, message):
        self.console.write(message)
        self.log.write(message)

logger = None

logConfig = {
    "version": 1,
    "formatters": {
        "standard": {
            "format": config.logFormat
        }
    },
    "handlers": {
        "default": {
            "level": config.logLevel,
            "formatter": "standard",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": config.logFileDir,
            "mode": "w"
        }
    },
    "loggers": {
        "tests": {
            "handlers": ['default'],
            "level": config.logLevel
        }
    }
}

def initialLogger():
    if not os.path.exists(config.logDir):
        os.mkdir(config.logDir)
    logging.config.dictConfig(logConfig)
    global logger
    logger = logging.getLogger("tests")
    variable.logger = logging.getLogger("tests")
