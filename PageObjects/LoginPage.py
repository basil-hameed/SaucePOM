"""
LoginPage contains the methods related to the login page only
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# import the data and locators
from TestData.data import SauceLabsData
from TestLocators.locators import SauceLabsLocators

class SauceLoginPage:

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def start(self):
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(SauceLabsData.url)
        return True
    
    def login(self):
        self.driver.find_element(by=By.ID, value=SauceLabsLocators.username_locator).send_keys(SauceLabsData.username)
        self.driver.find_element(by=By.ID, value=SauceLabsLocators.password_locator).send_keys(SauceLabsData.password)
        self.driver.find_element(by=By.ID, value=SauceLabsLocators.login_button_locator).click()
        return True
    
    def shutdown(self):
        self.driver.quit()
        return None
