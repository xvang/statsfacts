# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest
import warnings
 
class NewVisitorTest(unittest.TestCase):
 
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)
 
    def tearDown(self):
        self.browser.quit()
 
    def test_it_worked(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('Welcome to Django', self.browser.title)
        
        
        


with warnings.catch_warnings(record=True):
     unittest.main()