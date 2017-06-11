# -*- coding: utf8 -*-
 
import unittest
 
from scenarios.baidu_search import TestBaiDuSearch
 
 
# load test cases
baidu_search = unittest.TestLoader().loadTestsFromTestCase(TestBaiDuSearch)
 
# create test suite
test_suite = unittest.TestSuite([baidu_search])
 
# execute test suite
unittest.TextTestRunner(verbosity=2).run(test_suite)
