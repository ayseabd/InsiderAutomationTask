from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CareersPage(BasePage):
    LOCATIONS_BLOCK = (By.XPATH, "//*[contains(text(), 'Locations')]")
    TEAMS_BLOCK = (By.XPATH, "//*[contains(text(), 'calling')]")
    LIFE_AT_INSIDER_BLOCK = (By.XPATH, "//*[contains(text(), 'Life at Insider')]")

    def verify_locations_block(self):
        self.hover_element(*self.LOCATIONS_BLOCK)
        return self.find(*self.LOCATIONS_BLOCK).is_displayed()

    def verify_teams_block(self):
        self.hover_element(*self.TEAMS_BLOCK)
        return self.find(*self.TEAMS_BLOCK).is_displayed()

    def verify_life_at_insider_block(self):
        self.hover_element(*self.LIFE_AT_INSIDER_BLOCK)
        return self.find(*self.LIFE_AT_INSIDER_BLOCK).is_displayed()
