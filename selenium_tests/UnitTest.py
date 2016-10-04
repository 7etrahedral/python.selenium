import unittest
import allure
import pytest
from selenium.webdriver.common.keys import Keys
from proboscis import test
from SeleniumSetup import SeleniumSetup


class UnitTest(SeleniumSetup):

    @allure.feature('feature 1')
    @allure.story('story 1')
    @pytest.allure.testcase('test-case 1')
    @pytest.allure.issue('issue 1')
    @test
    def test_search_in_python_org(self):
        wd = self.wd
        wd.get("http:www.python.org")
        self.assertIn("Python", wd.title)
        e = wd.find_element_by_name("q")
        e.send_keys("pycon")
        e.send_keys(Keys.RETURN)
        assert "No results found." not in wd.page_source

if __name__ == "__main__":
    unittest.main()
