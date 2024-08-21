import time

from pages.careers_page import CareersPage
from pages.home_page import HomePage
from pages.lever_page import LeverPage
from pages.open_positions_page import OpenPositionsPage
from tests.base_test import BaseTest


class TestCheckInsiderJobOpenings(BaseTest):
    def test_check_insider_job_openings(self):
        # Visit useinsider, check homepage
        home_page = HomePage(self.driver)
        self.assertEqual(self.base_url, home_page.get_current_url(), "Insider Anasayfa Açılmadı")
        home_page.click_menu_company()
        home_page.click_sub_menu_careers()

        # Check careers page and locations, teams and life at insider block
        careers_page = CareersPage(self.driver)
        careers_page.verify_locations_block()
        self.assertTrue(careers_page.verify_locations_block(), "Locations bloğu görüntülenmiyor")
        careers_page.verify_teams_block()
        self.assertTrue(careers_page.verify_teams_block(), "Teams bloğu görüntülenmiyor")
        careers_page.verify_life_at_insider_block()
        self.assertTrue(careers_page.verify_life_at_insider_block(), "Life at Insider bloğu görüntülenmiyor")

        # Check open positions page
        open_positions_page = OpenPositionsPage(self.driver)
        self.driver.get(self.qa_jobs_url)
        open_positions_page.click_qa_jobs_button()
        time.sleep(4)
        open_positions_page.click_dropdown_location()
        time.sleep(4)
        open_positions_page.click_dropdown_location_select()
        time.sleep(4)
        open_positions_page.click_dropdown_arrow()
        open_positions_page.hover_job_area()
        open_positions_page.check_job_openings()
        open_positions_page.click_view_role_button()
        time.sleep(4)

        # Check Lever page
        lever_page = LeverPage(self.driver)
        if lever_page.switch_to_new_tab():
            lever_page.verify_lever_page()

            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
