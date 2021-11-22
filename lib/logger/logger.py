# -*- coding: utf-8 -*-
import logging.config
import os
import sys

from config import config

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
    # sys.stdout = open(config.stdout_file, 'w')