# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 10:57:03 2019

@author: YY
"""

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# =============================================================================
# driver = webdriver.Chrome()
# driver.get("http://www.python.org")
# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()
# =============================================================================

# =============================================================================
# driver = webdriver.Chrome()
# driver.get('http://weibo.com/login.php')
# print(driver.page_source)
# driver.close()
# =============================================================================

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
