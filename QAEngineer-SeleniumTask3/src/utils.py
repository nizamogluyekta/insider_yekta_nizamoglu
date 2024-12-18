from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.action_chains import ActionChains 
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from datetime import datetime
import unittest
import logging
from time import sleep


class SeleniumLibrary:
    def __init__(self, browser='chrome'):
        if browser == 'chrome':
            service = ChromeService(executable_path="./driver/chromedriver.exe")
            self.driver = webdriver.Chrome(service=service)
        elif browser == 'firefox':
            options = FirefoxOptions()
            options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"
            service = FirefoxService(executable_path="./driver/geckodriver.exe")
            self.driver = webdriver.Firefox(service=service, options=options)
        else:
            raise ValueError("Unsupported browser: {}".format(browser))
        self.wait = WebDriverWait(self.driver, 10)

    def open_url(self, url):
        self.driver.get(url)
        self.driver.maximize_window()

    def check_title(self, expected_title):
        actual_title = self.driver.title
        assert actual_title == expected_title, f"Expected title '{expected_title}', but got '{actual_title}'"

    def find_element(self, by, value):
        return self.wait.until(EC.presence_of_element_located((by, value)))
    
    def click_element_byXpath(self, value):
        element = self.find_element(By.XPATH, value)
        element.click()

    def search_text_in_page(self, text):
        element = self.driver.find_element(By.XPATH, f"//*[contains(text(), '{text}')]")
        text = element.get_attribute('textContent')
        return len(text) > 0

    def check_text_for_xpath(self, xpath, text):
        element = self.driver.find_element(By.XPATH, xpath)
        actual_text = element.text
        assert actual_text == text, f"Expected text '{text}', but got '{actual_text}'"

    def hover_and_click(self, xpath):
        element = self.find_element(By.XPATH, xpath)
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()
        sleep(2) # Wait for stability
        element.click()

    def switch_to_window(self, window_number):
        self.driver.switch_to.window(self.driver.window_handles[window_number])
    
    def close_browser(self):
        self.driver.quit()