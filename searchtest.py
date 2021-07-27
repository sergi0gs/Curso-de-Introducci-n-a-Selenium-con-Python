import sys
import os
import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver

class SearchTests(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path = './chromedriver.exe')
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('http://demo.onestepcheckout.com/')
    
    def test_search_tee(self):
        driver = self.driver
        search_field = driver.find_element_by_name('q')
        search_field.clear() # Limpiar el campo de busqueda

        search_field.send_keys('tee')
        #simulamos la escritura del teclado para poner "tee"
        
        search_field.submit()
        #envía los datos ('tee') para que la página muestre los resultados de "tee"

    def test_search_salt_shaker(self):
        driver = self.driver
        search_field = driver.find_element_by_name('q')
        
        search_field.send_keys('salt shaker')
        search_field.submit()

        products = driver.find_elements_by_xpath('//*[@id="top"]/body/div/div[2]/div[2]/div/div[2]/div[2]/div[3]/ul/li/div/h2/a')
        self.assertEqual(1, len(products))

    def tearDown(self) -> None:
        return super().tearDown()