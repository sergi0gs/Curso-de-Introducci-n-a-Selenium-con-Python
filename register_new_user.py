import unittest
from selenium import webdriver

class RegisterNewUse(unittest.TestCase):
    def setUp(self):
        #self.driver = webdriver.Chrome(executable_path = './chromedriver.exe')
        self.driver = webdriver.Chrome(executable_path = './chromedriver')
        driver = self.driver
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get('http://demo-store.seleniumacademy.com/')

    def test_new_user(self):
        driver = self.driver
        driver.find_element_by_xpath('//*[@id="header"]/div/div[2]/div/a/span[2]').click()
        driver.find_element_by_link_text('Log In').click()
       
        create_account_button = driver.find_element_by_xpath('//*[@id="login-form"]/div/div[1]/div[2]/a/span/span')
        # verificamos que el boton este habilitado
        self.assertTrue(create_account_button.is_displayed() and create_account_button.is_enabled())
        create_account_button.click()

        # Verificamos si estamos en la seccion de creacion de cuenta
        # Vamos a comparar: assertEqual
        self.assertEqual('Create New Customer Account', driver.title)

        first_name = driver.find_element_by_id('firstname')
        middle_name = driver.find_element_by_id('middlename')
        last_name = driver.find_element_by_id('lastname')
        email_address = driver.find_element_by_id('email_address')
        news_letter_subscription = driver.find_element_by_id('is_subscribed')
        password = driver.find_element_by_id('password')
        confirm_password = driver.find_element_by_id('confirmation')
        submit_button = driver.find_element_by_xpath('//*[@id="form-validate"]/div[2]/button/span/span')

        # Verificar que esten habilitados
        self.assertTrue(first_name.is_enabled()
        and last_name.is_enabled()
        and middle_name.is_enabled()
        and email_address.is_enabled()
        and news_letter_subscription.is_enabled()
        and password.is_enabled()
        and confirm_password.is_enabled()
        and submit_button.is_enabled())

        # Damos la informacion
        first_name.send_keys('Test')
        driver.implicitly_wait(2)

        middle_name.send_keys('Test')
        driver.implicitly_wait(2)

        last_name.send_keys('Test')
        driver.implicitly_wait(2)

        email_address.send_keys('Test@testinggmail.com')
        driver.implicitly_wait(2)

        news_letter_subscription.send_keys('Test')
        driver.implicitly_wait(2)

        password.send_keys('Test')
        driver.implicitly_wait(2)

        confirm_password.send_keys('Test')
        driver.implicitly_wait(2)

        submit_button.click()
        driver.implicitly_wait(2)

    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.close()

if __name__ == '__main__':
    unittest.main(verbosity=2)