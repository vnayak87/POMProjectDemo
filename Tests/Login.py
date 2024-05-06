import time
from selenium.webdriver.common.by import By
from selenium import webdriver
import unittest
from POMProjectDemo.Pages.loginPage import LoginPage
from POMProjectDemo.Pages.homePage import HomePage
import HtmlTestRunner
class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_valid(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")
        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()

        homepage = HomePage(driver)
        homepage.click_welcome()
        homepage.click_logout()

        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        print("Test Completed")

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/admin04/PycharmProjects/pythonProject/SampleProject/reports'))