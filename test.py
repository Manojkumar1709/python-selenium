import unittest
from selenium import webdriver

class TestWebsiteLoading(unittest.TestCase):
    def setUp(self):
        #self.driver = webdriver.Chrome()  # You can use any WebDriver you prefer
        chrome_driver_path = '/usr/bin/google-chrome'
        #self.driver = webdriver.Chrome(executable_path=chrome_driver_path)
        try:
            # Initialize Chrome WebDriver with the specified path
            self.driver = webdriver.Chrome(executable_path=chrome_driver_path)
            self.driver.implicitly_wait(10)
        except Exception as e:
            print("Error initializing Chrome WebDriver:", e)
        #self.driver.implicitly_wait(10)

    def test_website_load(self):
        print("Loading the website...")
        try:
            self.driver.get("https://atg.world")
            print("Website loaded successfully")
            result = "Test case is passed"
        except Exception as e:
            print("Failed to load the website")
            result = "Test case is failed"
        print(result)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
