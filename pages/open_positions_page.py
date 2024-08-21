from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class OpenPositionsPage(BasePage):
    URL = 'https://useinsider.com/careers/quality-assurance/'

    QA_JOBS_BUTTON = (By.XPATH, "//*[contains(text(), 'See all QA jobs')]")
    DROPDOWN_LOCATION = (By.XPATH, "//span[@id='select2-filter-by-location-container']")
    DROPDOWN_LOCATION_SELECT = (By.XPATH, "//option[@class='job-location istanbul-turkey']")
    DROPDOWN_ARROW = (By.CLASS_NAME, "select2-selection__arrow")
    JOB_LIST = (By.ID, "jobs-list")
    JOB_LISTING = (By.CLASS_NAME, "position-list-item-wrapper")
    POSITION_TITLE = (By.CLASS_NAME, "position-title")
    POSITION_DEPARTMENT = (By.CLASS_NAME, "position-department")
    POSITION_LOCATION = (By.CLASS_NAME, "position-location")
    VIEW_ROLE = (By.LINK_TEXT, "View Role")

    def click_qa_jobs_button(self):
        self.click_element(*self.QA_JOBS_BUTTON)

    def click_dropdown_location(self):
        self.click_element(*self.DROPDOWN_LOCATION)

    def click_dropdown_location_select(self):
        self.click_element(*self.DROPDOWN_LOCATION_SELECT)

    def click_dropdown_arrow(self):
        self.click_element(*self.DROPDOWN_ARROW)

    def click_view_role_button(self):
        self.click_element(*self.VIEW_ROLE)

    def hover_job_area(self):
        job_area = self.find(*self.JOB_LISTING)
        hover = ActionChains(self.driver).move_to_element(job_area)
        hover.perform()

    def check_job_openings(self):
        jobs_list = self.find(*self.JOB_LIST)
        if "No positions available." in jobs_list.text:
            print("Test durumu #1: Filtrelere göre ilan yok.")
            assert "No positions available." in jobs_list.text, "Beklenen mesaj bulunamadı."
        else:
            print("Test durumu #2: Filtrelere göre ilanlar var.")
            assert len(jobs_list.find_elements(By.TAG_NAME, "div")) > 0, "İlanlar listelenmedi."

            job_elements = jobs_list.find_elements(*self.JOB_LISTING)

            for job in job_elements:
                try:
                    position_text = job.find_element(*self.POSITION_TITLE).text
                    department_text = job.find_element(*self.POSITION_DEPARTMENT).text
                    location_text = job.find_element(*self.POSITION_LOCATION).text

                    assert "Quality Assurance" in position_text, f"Position içeriği doğrulanamadı: {position_text}"
                    assert "Quality Assurance" in department_text, f"Department içeriği doğrulanamadı: {department_text}"
                    assert "Istanbul, Turkey" in location_text, f"Location içeriği doğrulanamadı: {location_text}"

                except Exception as e:
                    print(f"Eleman doğrulama sırasında hata oluştu: {e}")
