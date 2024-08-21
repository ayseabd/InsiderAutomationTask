import unittest

from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait


class BasePage(unittest.TestCase):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    def find(self, *locator):
        return self.driver.find_element(*locator)

    def click_element(self, *locator):
        self.driver.find_element(*locator).click()

    def hover_element(self, *locator):
        element = self.find(*locator)
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()

    def get_current_url(self):
        return self.driver.current_url
