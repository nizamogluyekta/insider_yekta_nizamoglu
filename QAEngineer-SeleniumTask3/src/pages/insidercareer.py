from utils import *

def select_location_and_department(self, location_xpath, department_xpath, location_text, department_text):
        self.find_element(By.XPATH, location_xpath).click()
        self.driver.find_element(By.XPATH, f"//*[contains(text(), '{location_text}')]").click()
        self.find_element(By.XPATH, department_xpath).click()
        self.driver.find_element(By.XPATH, f"//*[contains(text(), '{department_text}')]").click()
