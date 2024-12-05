class CommerceCenterVerification:
    def __init__(self, commerce_page):
        self.commerce_page = commerce_page

    def check_catalog_modal_visibility(self):
        assert self.commerce_page.catalog_modal_page_became_visible()

    def check_catalog_modal_invisibility(self):
        assert not self.commerce_page.catalog_modal_page_became_visible()

    def check_choice_learning_modal_visibility(self):
        assert self.commerce_page.choice_learning_modal_page_became_visible()

    def check_choice_learning_modal_close(self):
        assert self.commerce_page.close_choice_learning_modal_page()

    def check_required_field_error(self):
        assert self.commerce_page.is_required_field_error_displayed()

    def check_feed_fields(self):
        assert self.commerce_page.field_feed_displayed()
        assert self.commerce_page.field_period_displayed()
        assert self.commerce_page.field_utm_displayed()

    def check_marketplace_fields(self):
        assert self.commerce_page.verify_marketplace_fields_visible()

    def check_manual_fields(self):
        assert self.commerce_page.field_category_displayed()
        assert self.commerce_page.field_feed_file_displayed()
        assert self.commerce_page.field_utm_displayed()
