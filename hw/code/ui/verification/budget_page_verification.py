class BudgetPageVerification:
    def __init__(self, budget_page):
        self.budget_page = budget_page

    def check_replenishment_modal_opened(self):
        assert self.budget_page.has_replenishment_modal_page_title()
        assert self.budget_page.modal_has_h2_content_title()
        assert self.budget_page.close_modal_page_became_visible()
        assert self.budget_page.submit_button_became_visible()
        assert self.budget_page.inputs_became_visible()

    def check_replenishment_modal_closed(self):
        assert self.budget_page.replenishment_modal_page_became_invisible()

    def check_error_message(self, expected_message):
        assert self.budget_page.get_error_message() == expected_message

    def check_amount_field_empty(self):
        assert self.budget_page.get_amount_value() == ''

    def check_amount_without_vat_field_empty(self):
        assert self.budget_page.get_amount_without_vat_value() == ''

    def check_vat_deduction(self, expected_value):
        assert self.budget_page.get_amount_without_vat_value() == expected_value

    def check_vat_addition(self, expected_value):
        assert self.budget_page.get_amount_value() == expected_value

    def check_vkpay_iframe_visible(self):
        assert self.budget_page.vkpay_iframe_became_visible()
