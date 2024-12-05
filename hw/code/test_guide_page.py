import allure

from base_case import BaseCase
from hw.code.ui.fixtures import guide_page


class TestGuide(BaseCase):

    def test_open_guide_modal(self, guide_page, guide_page_verification):
        with allure.step("Открытие модального окна и его проверка"):
            guide_page.click_guide_button()
            guide_page_verification.check_modal_is_displayed()
            guide_page.click_guide_close_button()

    def test_group_modal(self, guide_page, guide_page_verification):
        with allure.step("Открытие группы в модальном окне"):
            guide_page.click_guide_button()
            guide_page_verification.check_modal_is_displayed()
            guide_page.click_group_modal_button()
            guide_page_verification.check_inner_modal_is_displayed()

    def test_pixel_modal(self, guide_page, guide_page_verification):
        with allure.step("Открытие Pixel модального окна"):
            guide_page.click_guide_button()
            guide_page_verification.check_modal_is_displayed()
            guide_page.click_pixel_modal_button()
            guide_page_verification.check_inner_modal_is_displayed()

    def test_catalog_modal(self, guide_page, guide_page_verification):
        with allure.step("Открытие каталога в модальном окне"):
            guide_page.click_guide_button()
            guide_page_verification.check_modal_is_displayed()
            guide_page.click_catalog_modal_button()
            guide_page_verification.check_inner_modal_is_displayed()

    def test_mobile_modal(self, guide_page, guide_page_verification):
        with allure.step("Открытие мобильного модального окна"):
            guide_page.click_guide_button()
            guide_page_verification.check_modal_is_displayed()
            guide_page.click_mobile_modal_button()
            guide_page_verification.check_inner_modal_is_displayed()

    def test_lidforms_modal(self, guide_page, guide_page_verification):
        with allure.step("Открытие Lidforms модального окна"):
            guide_page.click_guide_button()
            guide_page_verification.check_modal_is_displayed()
            guide_page.click_lidforms_modal_button()
            guide_page_verification.check_inner_modal_is_displayed()

    def test_miniapps_modal(self, guide_page, guide_page_verification):
        with allure.step("Открытие Miniapps модального окна"):
            guide_page.click_guide_button()
            guide_page_verification.check_modal_is_displayed()
            guide_page.click_miniapps_modal_button()
            guide_page_verification.check_inner_modal_is_displayed()

    def test_music_modal(self, guide_page, guide_page_verification):
        with allure.step("Открытие Music модального окна"):
            guide_page.click_guide_button()
            guide_page_verification.check_modal_is_displayed()
            guide_page.click_music_modal_button()
            guide_page_verification.check_inner_modal_is_displayed()

    def test_video_modal(self, guide_page, guide_page_verification):
        with allure.step("Открытие Video модального окна"):
            guide_page.click_guide_button()
            guide_page_verification.check_modal_is_displayed()
            guide_page.click_video_modal_button()
            guide_page_verification.check_inner_modal_is_displayed()

    def test_dzen_modal(self, guide_page, guide_page_verification):
        with allure.step("Открытие Dzen модального окна"):
            guide_page.click_guide_button()
            guide_page_verification.check_modal_is_displayed()
            guide_page.click_dzen_modal_button()
            guide_page_verification.check_inner_modal_is_displayed()

    def test_click_pixel_video(self, guide_page, guide_page_verification):
        with allure.step("Клик по Pixel модальному окну и видео"):
            guide_page.click_guide_button()
            guide_page_verification.check_modal_is_displayed()
            guide_page.click_pixel_modal_button()
            guide_page_verification.check_inner_modal_is_displayed()
            guide_page.click_video_button()
            guide_page_verification.check_video_is_displayed()

    def test_click_pixel_platform(self, guide_page):
        with allure.step("Переход по платформе из Pixel модального окна"):
            guide_page.click_guide_button()
            guide_page.click_pixel_modal_button()
            guide_page.click_platform_button()
            guide_page.go_to_new_tab()
            assert self.driver.current_url.startswith('https://expert.vk.com/courses/')
