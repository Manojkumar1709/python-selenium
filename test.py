import unittest
from selenium import webdriver

class TestWebsiteLoading(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()  # You can use any WebDriver you prefer
        self.driver.implicitly_wait(10)

    def test_website_load(self):
        self.driver.get("https://atg.world")
        title = self.driver.title
        self.assertEqual(title, "ATG World - Discover Unique Places, Cultures, and Events")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
