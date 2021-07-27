import sys
import os
import unittest
from selenium import webdriver

class HomePageTests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = './chromedriver.exe')
        driver = self.driver
        driver.get('http://demo.onestepcheckout.com/')
        driver.maximize_window() #Que maximice la ventan porque puede haber elementos responsivos
        driver.implicitly_wait(15)

    def test_search_text_fild(self):
        # Asignamos a una variable el campo de busqueda
        search_field = self.driver.find_element_by_id("search")

    def test_search_text_field_by_name(self):
        search_field = self.driver.find_element_by_name("q")

    def test_seacg_text_field_by_class_name(self):
        search_field = self.driver.find_element_by_class_name("input-text")

    def test_search_button_enabled(self):
        button = self.driver.find_element_by_class_name("button")

    def test_count_of_images(self):
        banner_list = self.driver.find_element_by_class_name("cycle-slide")
        baners = banner_list.find_elements_by_tag_name("img")
        self.assertEqual(3, len(baners)) # Permite igualar y comparar si es la misma cantidad. 
        # Comparará si banners es igual a 3

    def test_vip_promo(self):
        vip_promo = self.driver.find_element_by_xpath('//*[@id="top"]/body/div/div[2]/div[2]/div/div/div[2]/div/ul/li[2]')

    def test_shopping_cart(self):
        shopping_cart_icon = self.driver.find_element_by_css_selector("div.header-minicart span.icon")

    def tearDown(self):
        self.driver.quit()
    
if __name__ == '__main__':
    unittest.main(verbosity=2)