from selenium import webdriver
from selenium.webdriver.common.keys import Keys

wd = webdriver.Firefox()
wd.get("http://www.python.org")
assert "Python" in wd.title
elem = wd.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in wd.page_source
wd.close()
