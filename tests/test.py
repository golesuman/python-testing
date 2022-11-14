import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


class ChromeSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.time = time

    # def test_search_in_python(self):
    #     driver = self.driver
    #     driver.get("https://www.python.org")
    #     self.assertIn("Python", driver.title, "title is not correct")
    #     elem = driver.find_element(
    #                         By.NAME, "q")

    #     elem.send_keys("getting started with python")
    #     driver.find_element(By.CSS_SELECTOR, "#submit").click()
    #     # elem.send_keys(Keys.RETURN)
    #     assert "https://www.python.org/search/?q=getting+started+with+python&submit=" == driver.current_url


    # def test_downloads_button(self):
    #     driver = self.driver
    #     driver.get("https://www.python.org/downloads/")
    #     element = driver.find_element(By.CSS_SELECTOR, "div.download-unknown > h1.call-to-action").text
    #     print(element)
    #     assert "Download the latest version of Python" == element
    
    def test_docs_button(self):
        driver = self.driver
        driver.get("https://python.org/")
        driver.find_element(By.CSS_SELECTOR, "#documentation").click()
        self.time.sleep(3)
        assert driver.current_url == "https://www.python.org/doc/" 




    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()