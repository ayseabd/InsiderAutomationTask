import unittest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseTest(unittest.TestCase):
    base_url = 'https://useinsider.com/'
    qa_jobs_url = 'https://useinsider.com/careers/quality-assurance/'

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--disable-notifications")
        self.driver = webdriver.Chrome(chrome_options)
        self.driver.maximize_window()
        self.driver.get(self.base_url)
        self.driver.implicitly_wait(10)

        # Çerezleri kabul etme işlemi
        try:
            cookie_accept_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, 'wt-cli-accept-all-btn'))
            )
            cookie_accept_button.click()
        except Exception as e:
            print("Çerez kabul butonu bulunamadı veya tıklanamadı:", e)

    def tearDown(self):
        self.driver.quit()
