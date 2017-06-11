# -*- coding: utf8 -*-

import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import WebDriverException


DEFAULT_WAIT = 3

class BaseCase(unittest.TestCase):
    """ inheriting the TestCase class"""
 
    @classmethod
    def setUpClass(cls):
        """test preparation"""
        chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
        cls.driver =  webdriver.Chrome(executable_path=chromedriver)
        cls.driver.implicitly_wait(3)
        cls.driver.set_window_size(450, 500)
 
    @classmethod
    def tearDownClass(cls):
        """clean up"""
        cls.driver.close()

    def find_ddt_element(self,elem_by,elem_val):
        return WebDriverWait(self.driver,10).until(lambda driver :self.driver.find_element(by = eval("By.%s"%elem_by),value = elem_val))

    def wait_for(self,function_with_assertion,timeout=DEFAULT_WAIT):
        start_time=time.time()
        while time.time()-start_time<timeout:
            try:
                return function_with_assertion
            except (AssertionError,WebDriverException):
                time.sleep(0.1)
        #最后试一次，如果还不行就抛出异常
        return function_with_assertion
