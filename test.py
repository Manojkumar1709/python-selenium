import unittest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import os 
import time  

class TestWebsiteLoading(unittest.TestCase):

    def setUp(self):
        if not os.getenv("PATH") or "geckodriver" not in os.getenv("PATH"):
            os.environ["PATH"] = os.pathsep.join([os.environ["PATH"], "/snap/bin/geckodriver"])

        options = Options()
        options.headless = True

        firefox_binary = "/usr/bin/firefox"

        try:
            # Launch the browser with potential fixes
            self.driver = webdriver.Firefox(options=options, executable_path=firefox_binary)
        except Exception as e:
            print(f"Failed to launch Firefox: {e}")
            self.tearDown()  
            raise 

        # Consider using WebDriverWait for dynamic content (explained later)
        # self.wait = WebDriverWait(self.driver, 10)  # Optional

    def test_website_load(self):
        print("Loading the website...")
        try:
            self.driver.get("https://atg.world")

            # Consider using WebDriverWait for dynamic content (explained later)
            # element = self.wait.until(EC.presence_of_element_located((By.ID, "some_unique_id")))

            print("Website loaded successfully")
            result = "Test case passed"
        except Exception as e:
            print(f"Failed to load the website: {e}")
            result = "Test case failed"
        print(result)

    def tearDown(self):
        if hasattr(self, 'driver'): 
            self.driver.quit()

if __name__ == "__main__":
    unittest.main()
