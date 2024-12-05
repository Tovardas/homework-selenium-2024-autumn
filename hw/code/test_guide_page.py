import time

import pytest
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base_case import BaseCase
from hw.code.ui.fixtures import guide_page
from ui.locators.guide_page_locators import GuidePageLocators


class TestGuide(BaseCase):
    def test_open_guide_modal(self, guide_page):
        guide_page.click_guide_button()
        assert guide_page.modal_is_displayed()
        guide_page.click_guide_close_button()

    def test_group_modal(self, guide_page):
        guide_page.click_guide_button()
        assert guide_page.modal_is_displayed()
        guide_page.click_group_modal_button()
        assert guide_page.inner_modal_is_displayed()

    def test_pixel_modal(self, guide_page):
        guide_page.click_guide_button()
        assert guide_page.modal_is_displayed()
        guide_page.click_pixel_modal_button()
        assert guide_page.inner_modal_is_displayed()

    def test_catalog_modal(self, guide_page):
        guide_page.click_guide_button()
        assert guide_page.modal_is_displayed()
        guide_page.click_catalog_modal_button()
        assert guide_page.inner_modal_is_displayed()

    def test_mobile_modal(self, guide_page):
        guide_page.click_guide_button()
        assert guide_page.modal_is_displayed()
        guide_page.click_mobile_modal_button()
        assert guide_page.inner_modal_is_displayed()

    def test_lidforms_modal(self, guide_page):
        guide_page.click_guide_button()
        assert guide_page.modal_is_displayed()
        guide_page.click_lidforms_modal_button()
        assert guide_page.inner_modal_is_displayed()

    def test_miniapps_modal(self, guide_page):
        guide_page.click_guide_button()
        assert guide_page.modal_is_displayed()
        guide_page.click_miniapps_modal_button()
        assert guide_page.inner_modal_is_displayed()

    def test_music_modal(self, guide_page):
        guide_page.click_guide_button()
        assert guide_page.modal_is_displayed()
        guide_page.click_music_modal_button()
        assert guide_page.inner_modal_is_displayed()

    def test_video_modal(self, guide_page):
        guide_page.click_guide_button()
        assert guide_page.modal_is_displayed()
        guide_page.click_video_modal_button()
        assert guide_page.inner_modal_is_displayed()

    def test_dzen_modal(self, guide_page):
        guide_page.click_guide_button()
        assert guide_page.modal_is_displayed()
        guide_page.click_dzen_modal_button()
        assert guide_page.inner_modal_is_displayed()

    def test_click_pixel_video(self):
        guide_page.click_guide_button()
        assert guide_page.modal_is_displayed()
        guide_page.click_pixel_modal_button()
        assert guide_page.inner_modal_is_displayed()
        guide_page.click_video_button()
        assert guide_page.video_is_displayed()

    def test_click_pixel_platform(self):
        guide_page.click_guide_button()
        assert guide_page.modal_is_displayed()
        guide_page.click_pixel_modal_button()
        assert guide_page.inner_modal_is_displayed()
        guide_page.click_platform_button()
        guide_page.go_to_new_tab()
        assert self.driver.current_url.startswith('https://expert.vk.com/courses/')




