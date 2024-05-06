from selenium.webdriver.common.by import By


class HomePage():

    def __init__(self,driver):
        self.driver = driver

        self.welcome_link_CSS_SELECTOR = ".oxd-userdropdown-tab"
        self.logout_link_CSS_SELECTOR = "a[href*='logout']"

    def click_welcome(self):
        self.driver.find_element((By.CSS_SELECTOR),self.welcome_link_CSS_SELECTOR).click()

    def click_logout(self):
        self.driver.find_element((By.CSS_SELECTOR),self.logout_link_CSS_SELECTOR).click()



