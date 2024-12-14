
from mylib import *

# Configure logging
logging.basicConfig(filename='test_log.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

class TestSeleniumLibrary(unittest.TestCase):

    def setUp(self):
        selectedBrowser = "chrome"
        self.selenium_lib = SeleniumLibrary(selectedBrowser)
        logging.info("Browser setup completed. Browser: " + selectedBrowser)

    def tearDown(self):
        result = self.defaultTestResult()
        self._feedErrorsToResult(result, self._outcome.errors)
        error = self._outcome.errors

        if error and error[-1][1] is not None:  # if there is an error
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            screenshot_name = f'screenshot_{timestamp}.png'
            self.selenium_lib.driver.save_screenshot(screenshot_name)
            logging.error(f"Test failed. Screenshot saved as {screenshot_name}.")
            logging.error(f"Error: {error[-1][1]}")
        self.selenium_lib.close_browser()
        logging.info("Browser closed.")

    def test_QA_engineer(self):
        #Part 1
        self.selenium_lib.open_url("https://useinsider.com/")
        self.selenium_lib.check_title("#1 Leader in Individualized, Cross-Channel CX — Insider")
        logging.info("We are in the correct page.(home page)")
        #Part 2
        self.selenium_lib.click_element_byXpath("/html/body/nav/div[2]/div/ul[1]/li[6]/a")
        logging.info("Clicked on Company.")
        self.selenium_lib.click_element_byXpath("/html/body/nav/div[2]/div/ul[1]/li[6]/div/div[2]/a[2]")
        logging.info("Clicked on Careers.")
        self.assertTrue(self.selenium_lib.search_text_in_page("Ready to disrupt?"), "Text not found in the page")
        self.assertTrue(self.selenium_lib.search_text_in_page("Our story"), "Text not found in the page")
        self.assertTrue(self.selenium_lib.search_text_in_page("Find your calling"), "Text not found in the page")
        self.assertTrue(self.selenium_lib.search_text_in_page("Our Locations"), "Text not found in the page")
        self.assertTrue(self.selenium_lib.search_text_in_page("Life at Insider"), "Text not found in the page")
        logging.info("All expected sections are visible in the page.")
        # self.selenium_lib.close_browser()
        #Part 3
        self.selenium_lib.open_url("https://useinsider.com/careers/quality-assurance/")
        self.selenium_lib.check_title("Insider quality assurance job opportunities")
        logging.info("We are in the correct page.(carrers/quality-assurance)")
        self.selenium_lib.driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div/span/div/div[2]/a[1]").click()
        self.selenium_lib.click_element_byXpath("/html/body/div[1]/section[1]/div/div/div/div[1]/div/section/div/div/div[1]/div/div/a")
        logging.info("Clicked on See all QA jobs")
        sleep(15) # Wait for the page to load
        self.selenium_lib.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        logging.info("Scrolled down to the bottom of the page.")
        sleep(5) # Wait for stability
        self.selenium_lib.select_location_and_department("/html/body/section[2]/div/div/div[2]/div/form/div[1]/span/span[1]/span/span[1]", "/html/body/section[2]/div/div/div[2]/div/form/div[2]/span/span[1]/span/span[1]", "Istanbul, Turkey", "Quality Assurance")
        logging.info("Selected location and department.")
        sleep(10) # Wait for stability
        self.assertTrue(self.selenium_lib.search_text_in_page("Open Positions"), "Text not found in the page")
        logging.info("Open Positions section is visible in the page.")
        #Part 4
        self.selenium_lib.check_text_for_xpath("/html/body/section[3]/div/div/div[2]/div[1]/div/span","Quality Assurance")
        self.selenium_lib.check_text_for_xpath("/html/body/section[3]/div/div/div[2]/div[1]/div/div","Istanbul, Turkey")
        self.selenium_lib.check_text_for_xpath("/html/body/section[3]/div/div/div[2]/div[2]/div/span","Quality Assurance")
        self.selenium_lib.check_text_for_xpath("/html/body/section[3]/div/div/div[2]/div[2]/div/div","Istanbul, Turkey")
        self.selenium_lib.check_text_for_xpath("/html/body/section[3]/div/div/div[2]/div[3]/div/span","Quality Assurance")
        self.selenium_lib.check_text_for_xpath("/html/body/section[3]/div/div/div[2]/div[3]/div/div","Istanbul, Turkey")
        logging.info("List of the open positions are checked.(3 positions visible)")
        #Part 5
        self.selenium_lib.hover_and_click("/html/body/section[3]/div/div/div[2]/div[1]/div/a")
        logging.info("Clicked on the first open position.")
        sleep(5) # Wait for the page to load
        self.selenium_lib.switch_to_window(1)
        logging.info("Switched to the new tab.")
        self.assertIn("jobs.lever.co", self.selenium_lib.driver.current_url, "URL is not correct")
        logging.info("URL is correct.")
        self.selenium_lib.close_browser()
        logging.info("Test is completed.")




if __name__ == '__main__':
    unittest.main()
    
