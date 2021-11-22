# -*- coding: utf-8 -*-
from logging import log
import pytest
import sys
import argparse
import os

from lib.logger.logger import *


if __name__ == "__main__":
    testCaseName = ""

    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--testcase")
    args = parser.parse_args()
    
    initialLogger()

    # setup test case name
    if args.testcase:
        testCaseName = args.testcase
        testSuiteName = os.path.join(os.getcwd(), "tests", "test_%s.py" % (testCaseName))
        # logger.info("Running specific test suite: %s, test suite: %s" % (testCaseName, testSuiteName))
    else:
        pass
        # logger.info("Running all tests")

    # setup pytest cmd
    cmd = ""
    if testCaseName:
        cmd = pytest.main(["-v", testSuiteName])
    else:
        cmd = pytest.main(["-v"])

    # execute pytest cmd
    sys.exit(cmd)