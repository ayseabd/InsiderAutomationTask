from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class HomePage(BasePage):
    COOKIE_ACCEPT_BUTTON = (By.ID, 'wt-cli-accept-all-btn')
    MENU_COMPANY = (By.LINK_TEXT, "Company")
    MENU_CAREERS = (By.LINK_TEXT, "Careers")

    def click_accept_cookies(self):
        self.click_element(*self.COOKIE_ACCEPT_BUTTON)

    def click_menu_company(self):
        self.click_element(*self.MENU_COMPANY)

    def click_sub_menu_careers(self):
        self.click_element(*self.MENU_CAREERS)
