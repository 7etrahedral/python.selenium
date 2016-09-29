import unittest
from selenium import webdriver
from proboscis import before_class
from proboscis import after_class


class SeleniumSetup(unittest.TestCase):

    def seleniumSetup(self):
        self.wd = webdriver.Firefox()

    @before_class
    def setUp(self):
        self.seleniumSetup()

    @after_class
    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()