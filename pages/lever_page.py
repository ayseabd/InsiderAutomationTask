from pages.base_page import BasePage


class LeverPage(BasePage):
    LEVER_URL_BASE = "https://jobs.lever.co/useinsider"

    def verify_lever_page(self):
        # Lever sayfasının base URL'ini doğrula
        new_url = self.get_current_url()
        self.assertTrue(new_url.startswith(self.LEVER_URL_BASE),
                        f"Beklenen base URL '{self.LEVER_URL_BASE}' ile '{new_url}' eşleşmiyor")
        print("'View Role' button redirect to the Lever Application form page successfully.")

    def switch_to_new_tab(self):
        # Mevcut sekmeleri al
        all_tabs = self.driver.window_handles
        if len(all_tabs) > 1:
            # Yeni sekmeye geç
            self.driver.switch_to.window(all_tabs[-1])
            return True
        else:
            print("Yeni bir sekme açılmadı.")
            return False
