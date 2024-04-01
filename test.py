import unittest
from selenium import webdriver

class TestWebsiteLoading(unittest.TestCase):
    def setUp(self):
        #self.driver = webdriver.Chrome()  
        #self.driver = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver')  
        geckodriver_path = '/usr/local/bin/geckodriver'
        service = Service(geckodriver_path)
        self.driver = webdriver.Firefox(service=service)
        self.driver.implicitly_wait(10)

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
