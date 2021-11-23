# -*- coding: utf-8 -*-
import pytest
import sys
import argparse
import os

from lib.logger.logger import *
from lib.utility import DataLoader


if __name__ == "__main__":
    testCaseName = ""

    # Parse arguments from cli
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--testcase")
    args = parser.parse_args()
    
    # Initial logger
    initialLogger()
    sys.stdout = TerminalOutput()

    # Load xpath from json
    dataLoader = DataLoader()
    dataLoader.loadJsonXpath()

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
        cmd = pytest.main(["-v", "-s", testSuiteName])
    else:
        cmd = pytest.main(["-v", "-s"])

    # execute pytest cmd
    sys.exit(cmd)