import unittest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

class TestWebsiteLoading(unittest.TestCase):
    def setUp(self):
        options = Options()
        options.headless = True
        # Launch the browser with headless options
        self.driver = webdriver.Firefox(options=options)
        self.driver = webdriver.Firefox()  # You can use any WebDriver you prefer
        self.driver.implicitly_wait(50)

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
