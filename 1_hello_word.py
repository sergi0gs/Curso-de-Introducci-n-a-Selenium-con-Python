# Para ejecutar el programa es necesario tener una versión de Python entre 3.6 y 3.8
# Instalar selenium y pyunitreport
# Se sugiere usar Anaconda para gestionar los entornos virtuales

import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver

class HelloWorld(unittest.TestCase):
    #Preprar el entorno de la prueba
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path = r'C:\SERGIO\PLATZI\Curso de Introducción a Selenium con Python\chromedriver.exe')
        driver = cls.driver
        driver.implicitly_wait(10) #Esper 10 segundos antes de la siguiente accion

    # Acciones para la automatización
    def test_hello_world(self):
        driver = self.driver
        driver.get('https://www.platzi.com')

    def test_vist_wikipedia(self):
        driver = self.driver
        driver.get('https://www.wikipedia.org')

    def test_instore_view(self):
        driver = self.driver
        driver.get('https://www.instoreview.cl/')

    # Acciones al terminar la automatización
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit() # Cerrar la ventana del navegador

if __name__ == "__main__":
    unittest.main(verbosity = 2, 
                   testRunner = HTMLTestRunner(output = 'reportes', 
                                report_name = 'hello-world-report'))