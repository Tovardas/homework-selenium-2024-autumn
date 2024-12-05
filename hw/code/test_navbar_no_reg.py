from selenium.webdriver.support.ui import WebDriverWait

from base_case import BaseCase


class TestNavbarNoReg(BaseCase):
    def test_href_to_news(self, navbar_no_reg):
        navbar_no_reg.click_news_button()
        assert self.is_opened('https://ads.vk.com/news')

    def test_href_to_cases(self, navbar_no_reg):
        navbar_no_reg.click_cases_button()
        assert self.is_opened('https://ads.vk.com/cases')

    def test_href_to_forum(self, navbar_no_reg):
        navbar_no_reg.click_forum_button()
        assert self.is_opened('https://ads.vk.com/upvote')

    def test_href_to_auth(self, navbar_no_reg):
        navbar_no_reg.click_auth_button()
        WebDriverWait(self.driver, 10).until(
            lambda d: d.current_url.startswith('https://id.vk.com/auth')
        )
        current_url = self.driver.current_url
        assert current_url.startswith("https://id.vk.com/auth")

    def test_href_to_mainpage(self, navbar_no_reg):
        navbar_no_reg.click_news_button()
        assert self.is_opened('https://ads.vk.com/news')
        navbar_no_reg.click_logo_button()
        assert self.is_opened('https://ads.vk.com')

    def test_href_to_monetize(self, navbar_no_reg):
        navbar_no_reg.click_monetize_button()
        navbar_no_reg.go_to_new_tab()

        assert self.driver.current_url.startswith('https://ads.vk.com/partner')
