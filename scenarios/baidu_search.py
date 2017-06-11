# -*- coding: utf8 -*-


import sys
reload(sys)
sys.setdefaultencoding("utf-8")
from ddt import ddt, data, unpack
from library.GetData import get_csv_data
from scenarios.base_case import BaseCase
 
 

@ddt
class TestBaiDuSearch(BaseCase):
    """ inheriting the BaseCase class"""

    @data(*get_csv_data('./data/test_case.csv'))
    @unpack
    def test_search(self, target_url, elem_by,elem_val, search_value):
        """test case for scenario a"""
        driver = self.driver
        driver.get(target_url)

        """run baidu search step"""
        input_elem = self.find_ddt_element(elem_by,elem_val)
        input_elem.clear()
        input_elem.send_keys(search_value)
        input_elem.submit()


        """assert search result"""
        self.wait_for(self.assertIn(search_value,driver.title,"FACT%s,EXPECT:%s"%(driver.title,search_value)))
        self.wait_for(self.assertIn(search_value,driver.page_source,"FACT%s,EXPECT:%s"%(driver.page_source,search_value)))
