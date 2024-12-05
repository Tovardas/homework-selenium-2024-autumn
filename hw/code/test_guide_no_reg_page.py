import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
from base_case import BaseCase
import time

class TestGuideNoRegPage(BaseCase):
    def test_href_to_materials(self, guide_no_reg_page):
        guide_no_reg_page.click_materials_button()
        assert self.is_opened('https://ads.vk.com/insights')


    def test_href_to_events(self, guide_no_reg_page):
        guide_no_reg_page.click_events_button()
        assert self.is_opened('https://ads.vk.com/events')

    def test_href_to_videos(self, guide_no_reg_page):
        guide_no_reg_page.click_videos_button()
        guide_no_reg_page.go_to_new_tab()

        assert self.driver.current_url.startswith('https://expert.vk.com/catalog/courses/')

    def test_href_to_certification(self, guide_no_reg_page):
        guide_no_reg_page.click_certification_button()
        guide_no_reg_page.go_to_new_tab()

        assert self.driver.current_url.startswith('https://expert.vk.com/certification/')

    def test_materials_tags_redirect(self, guide_no_reg_page):
        guide_no_reg_page.click_materials_button()
        assert self.is_opened('https://ads.vk.com/insights')
        guide_no_reg_page.click_materials_card()
        assert self.is_opened('https://ads.vk.com/insights/rekomendacii-po-rabote-s-reklamnym-byudzhetom')
        guide_no_reg_page.click_materials_tag()
        assert self.is_opened('https://ads.vk.com/tags/marketing')

    def test_materials_content(self, guide_no_reg_page):
        guide_no_reg_page.click_materials_button()
        assert self.is_opened('https://ads.vk.com/insights')
        guide_no_reg_page.click_materials_card()
        assert self.is_opened('https://ads.vk.com/insights/rekomendacii-po-rabote-s-reklamnym-byudzhetom')
        guide_no_reg_page.click_materials_content()
        assert guide_no_reg_page.header_became_visible()
        assert self.is_opened('https://ads.vk.com/insights/rekomendacii-po-rabote-s-reklamnym-byudzhetom#reasons')
        guide_no_reg_page.click_materials_cabinet_button()
        guide_no_reg_page.go_to_new_tab()
        assert self.driver.current_url.startswith("https://id.vk.com/auth")

    def test_materials_paginator(self, guide_no_reg_page):
        guide_no_reg_page.click_materials_button()
        assert self.is_opened('https://ads.vk.com/insights')
        guide_no_reg_page.click_pagination_number()
        assert self.query_parameter_matches('p', 3)
        guide_no_reg_page.click_pagination_right()
        assert self.query_parameter_matches('p', 4)
        guide_no_reg_page.click_pagination_left()
        assert self.query_parameter_matches('p', 3)



    def test_events_card_old(self, guide_no_reg_page):
        guide_no_reg_page.click_events_button()
        guide_no_reg_page.click_events_card_old()
        assert self.is_opened('https://ads.vk.com/events/moderation-rules-webinar')
        #assert guide_no_reg_page.event_contains_video()

    def test_events_card_new(self, guide_no_reg_page):
        guide_no_reg_page.click_events_button()
        guide_no_reg_page.click_events_card_new()
        assert self.is_opened('https://ads.vk.com/events/prodvizhenie-novogodnie-prazdniki-vebinar-0512')



