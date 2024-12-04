from base_case import BaseCase

CUSTOM_AUDIENCE_NAME = "Tester Audience"
SOURCE_NAME = "Ключевые фразы"
KEY_PHRASES = ["business", "tasks"]


class TestAudiencePage(BaseCase):
    def test_create_audience_modal_page_opened(self, audience_page):
        audience_page.click_create_audience_button()
        assert audience_page.create_audience_modal_page_became_visible()
        assert audience_page.audience_name_input_became_visible()
        assert audience_page.sidebar_sign_became_visible()
        assert audience_page.add_source_button_became_visible()
        assert audience_page.footer_buttons_became_visible()
        assert audience_page.cross_button_became_visible()

    def test_create_audience_modal_page_closed(self, audience_page):
        audience_page.click_create_audience_button()
        audience_page.click_cross_button()
        assert audience_page.create_audience_modal_page_became_invisible()
        audience_page.click_create_audience_button()
        audience_page.click_cancel_button()
        assert audience_page.create_audience_modal_page_became_invisible()

    def test_error_long_audience_name(self, audience_page):
        audience_page.click_create_audience_button()
        audience_page.enter_audience_name('мяу' * 255)
        assert audience_page.get_error() == audience_page.ERROR_TOO_LONG_AUDIENCE_NAME

    def test_add_source_modal_page_became_visible(self, audience_page):
        audience_page.click_create_audience_button()
        audience_page.click_add_source_button()
        assert audience_page.add_source_modal_page_became_visible()
        assert audience_page.source_items_became_visible()

    def test_add_source_by_key_phrases(self, audience_page):
        audience_page.click_create_audience_button()
        audience_page.click_add_source_button()
        audience_page.select_source(SOURCE_NAME)
        audience_page.enter_key_phrases(KEY_PHRASES)
        audience_page.click_modal_page_submit_button()
        source_card_content = audience_page.get_source_card_content()
        for key_phrase in KEY_PHRASES:
            assert key_phrase in source_card_content

    def test_add_source_modal_page_became_invisible(self, audience_page):
        audience_page.click_create_audience_button()
        audience_page.click_add_source_button()
        assert audience_page.add_source_modal_page_became_visible()
        assert audience_page.source_items_became_visible()
        audience_page.click_cancel_source_button()
        assert audience_page.add_source_modal_page_became_invisible()

    def test_create_and_delete_audience(self, audience_page):
        audience_page.click_create_audience_button()
        audience_page.click_add_source_button()
        audience_page.select_source(SOURCE_NAME)
        audience_page.enter_key_phrases(KEY_PHRASES)
        audience_page.click_modal_page_submit_button()
        audience_page.enter_audience_name(CUSTOM_AUDIENCE_NAME)
        audience_page.click_modal_page_submit_button()
        assert audience_page.get_created_audience_title() == CUSTOM_AUDIENCE_NAME

        audience_page.hover_and_click_delete()
        assert audience_page.delete_confirm_modal_became_visible()
        audience_page.click_delete_confirm_button()
        assert audience_page.audience_item_became_invisible()

    def test_try_to_find_audience_success(self, audience_page):
        audience_page.click_create_audience_button()
        audience_page.click_add_source_button()
        audience_page.select_source(SOURCE_NAME)
        audience_page.enter_key_phrases(KEY_PHRASES)
        audience_page.click_modal_page_submit_button()
        audience_page.enter_audience_name(CUSTOM_AUDIENCE_NAME)
        audience_page.click_modal_page_submit_button()
        assert audience_page.get_created_audience_title() == CUSTOM_AUDIENCE_NAME

        audience_page.seach_audience_by_name(CUSTOM_AUDIENCE_NAME)
        assert audience_page.audience_item_became_visible()

        audience_page.hover_and_click_delete()
        assert audience_page.delete_confirm_modal_became_visible()
        audience_page.click_delete_confirm_button()
        assert audience_page.audience_item_became_invisible()

    def test_try_to_find_audience_error(self, audience_page):
        audience_page.click_create_audience_button()
        audience_page.click_add_source_button()
        audience_page.select_source(SOURCE_NAME)
        audience_page.enter_key_phrases(KEY_PHRASES)
        audience_page.click_modal_page_submit_button()
        audience_page.enter_audience_name(CUSTOM_AUDIENCE_NAME)
        audience_page.click_modal_page_submit_button()
        assert audience_page.get_created_audience_title() == CUSTOM_AUDIENCE_NAME

        audience_page.seach_audience_by_name('ERROR')
        assert audience_page.audience_item_became_invisible()

        audience_page.seach_audience_by_name(CUSTOM_AUDIENCE_NAME)
        assert audience_page.audience_item_became_visible()

        audience_page.hover_and_click_delete()
        assert audience_page.delete_confirm_modal_became_visible()
        audience_page.click_delete_confirm_button()
        assert audience_page.audience_item_became_invisible()
