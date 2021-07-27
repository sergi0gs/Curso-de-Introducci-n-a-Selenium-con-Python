import sys
import os
import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver

#sirve como excepción para los assertions cuando queremos
#validar la presencia de un elemento
from selenium.common.exceptions import NoSuchElementException

#ayuda a llamar a las excepciones que queremos validar
from selenium.webdriver.common.by import By 

class AssertionsTests(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path = './chromedriver.exe')
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('http://demo.onestepcheckout.com/')
    
    def test_search_field(self):
        self.assertTrue(self.is_element_present(By.Name, 'q'))


    def tearDown(self) -> None:
        return super().tearDown()

    #para saber si está presente el elemento
	#how: tipo de selector
	#what: el valor que tiene
    def is_element(self, how, what):
        try: 
            self.driver.find_element(by = how, value = what)
        except NoSuchElementException as variable:
            return False
        return True
