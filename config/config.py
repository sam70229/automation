# -*- coding: utf-8 -*-
import os
from datetime import datetime
import sys

sys_platform = sys.platform

## Chrome driver config

chrome_version = "96"
chrome_bin_filename = {
    "darwin": "chromedriver_darwin_%s" % (chrome_version),
    "win32": "chromedriver_%s.exe" % (chrome_version),
    "linux": "chromedriver_linux_%s" % (chrome_version)}
chromeDriverExecutePath = os.path.join(os.getcwd(), 'bin', chrome_bin_filename[sys_platform])

## Log config

logLevel = "INFO"
logFileName = "log_output.log"
logRootDir = os.path.join(os.getcwd(), "logs")
logDir = os.path.join(logRootDir, datetime.now().strftime("%Y_%m_%d_%H_%M_%S"))
logFileDir = os.path.join(logDir, logFileName)
logFormat = '%(asctime)s [%(levelname)s] %(filename)s:%(lineno)d %(funcName)s - %(message)s'
logDatefmt = '%Y%m%d %H:%M:%s'

#Console Log

consoleLogName = "console_log.log"
consoleLogFile = os.path.join(logDir, consoleLogName)


## Screenshot

screenshotFilepath = os.path.join(logDir, "fail_screenshot.png")


## Data

jsonDataPath = os.path.join(os.getcwd(), "data", "data.json")