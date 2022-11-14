from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import unittest
import time


class GoogleSearchTest(unittest.TestCase):

    def setUp(self) -> None:
        options = webdriver.ChromeOptions()
        options.add_argument("--lang=en-us")

        self.driver = webdriver.Chrome(options=options)


    def test_search_test(self):
        url = 'https://google.com/'
        driver = self.driver
        driver.get(url)
        self.assertIn("Google", driver.title)
        driver.find_element(By.CSS_SELECTOR, "#SIvCob > a").click()
        element = driver.find_element(By.CSS_SELECTOR, \
                                     "body > div.L3eUgb > div.o3j99.ikrT4e.om7nvf > \
                                     form > div:nth-child(1) > div.A8SBwf > \
                                     div.RNNXgb > div > div.a4bIc > input")
        element.send_keys("Indian cricket team")
        element.send_keys(Keys.ENTER)
        all_button = driver.find_element(By.CSS_SELECTOR, "div.MUFPAc > div.hdtb-mitem.hdtb-msel").text
        assert all_button == "All"

    def test_news_button(self):
        driver = self.driver
        driver.get("https://www.google.com")
        driver.find_element(By.CSS_SELECTOR, "#SIvCob > a").click()

        element = driver.find_element(By.CSS_SELECTOR, \
                                     "body > div.L3eUgb > div.o3j99.ikrT4e.om7nvf > \
                                     form > div:nth-child(1) > div.A8SBwf > \
                                     div.RNNXgb > div > div.a4bIc > input")
        element.send_keys("Indian cricket team")
        element.send_keys(Keys.ENTER)
        news_button = driver.find_element(By.CSS_SELECTOR, "#hdtb-msb > div:nth-child(1) > div > div:nth-child(2) > a").text
        # assert news_button == "News"
        print(news_button)


    def tearDown(self) -> None:
        self.driver.close()

if __name__ == "__main__":
    unittest.main()