import json
import os
import platform
import random
import subprocess
import sys
import time
import urllib.parse
from pathlib import Path
from argparse import ArgumentParser
from datetime import date, datetime, timedelta
from notifiers import get_notifier
from typing import Union, List
import copy
import traceback

import ipapi
import requests
from func_timeout import FunctionTimedOut, func_set_timeout
from random_word import RandomWords

from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import (ElementNotInteractableException,
                                        NoAlertPresentException,
                                        NoSuchElementException,
                                        SessionNotCreatedException,
                                        TimeoutException,
                                        UnexpectedAlertPresentException,
                                        JavascriptException,
                                        ElementNotVisibleException)
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options

from pyvirtualdisplay import Display
import zipfile


browser = None
firefoxOptions = Options()
firefoxOptions.add_argument("-headless")

try:
    browser = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver', service=Service(GeckoDriverManager().install()), options=firefoxOptions)
except Exception:
    browser = webdriver.Firefox(options=firefoxOptions)
	
def test_func(browser):
    browser.get('https://www.linuxhint.com')
    print('Title: %s' % browser.title)
    browser.quit()
 
test_func(browser)
