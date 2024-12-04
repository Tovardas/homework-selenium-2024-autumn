from base_case import BaseCase
import time

class TestBudgetPage(BaseCase):

    def test_is_opened_replenishment_modal_page(self, budget_page):
        budget_page.click_replenish_budget_button()
        assert budget_page.has_replenishment_modal_page_title()
        assert budget_page.modal_has_h2_content_title()
        assert budget_page.close_modal_page_became_visible()
        assert budget_page.submit_button_became_visible()
        assert budget_page.inputs_became_visible()

    def test_is_closed_replenishment_modal_page(self, budget_page):
        budget_page.click_replenish_budget_button()
        budget_page.close_replenishment_modal_page()
        assert budget_page.replenishment_modal_page_became_invisible()

    def test_is_error_too_little_amount(self, budget_page):
        budget_page.click_replenish_budget_button()
        budget_page.enter_amount(budget_page.MIN_AMOUNT - 1)
        budget_page.click_submit_button()
        assert budget_page.get_error_message() == budget_page.ERROR_TOO_LITTLE_AMOUNT

    def test_is_error_too_little_amount_without_vat(self, budget_page):
        budget_page.click_replenish_budget_button()
        budget_page.enter_amount_without_vat(budget_page.MIN_AMOUNT_WITHOUT_VAT - 1)
        budget_page.click_submit_button()
        assert budget_page.get_error_message() == budget_page.ERROR_TOO_LITTLE_AMOUNT

    def test_is_error_too_large_amount(self, budget_page):
        budget_page.click_replenish_budget_button()
        budget_page.enter_amount(budget_page.MAX_AMOUNT + 1)
        budget_page.click_submit_button()
        assert budget_page.get_error_message() == budget_page.ERROR_TOO_LARGE_AMOUNT

    def test_is_error_too_large_amount_without_vat(self, budget_page):
        budget_page.click_replenish_budget_button()
        budget_page.enter_amount_without_vat(budget_page.MAX_AMOUNT_WITHOUT_VAT + 1)
        budget_page.click_submit_button()
        assert budget_page.get_error_message() == budget_page.ERROR_TOO_LARGE_AMOUNT

    def test_enter_non_numeric_amount(self, budget_page):
        budget_page.click_replenish_budget_button()
        budget_page.enter_amount('letters $#!!#*&(!)!_')
        assert budget_page.get_amount_value() == ''

    def test_enter_non_numeric_amount_without_vat(self, budget_page):
        budget_page.click_replenish_budget_button()
        budget_page.enter_amount_without_vat('SLOVNO... !@#$%^&')
        assert budget_page.get_amount_without_vat_value() == ''

    def test_vat_deduction(self, budget_page):
        budget_page.click_replenish_budget_button()
        budget_page.enter_amount(600)
        assert budget_page.get_amount_without_vat_value() == '500 ₽'

    def test_vat_addition(self, budget_page):
        budget_page.click_replenish_budget_button()
        budget_page.enter_amount_without_vat(800)
        assert budget_page.get_amount_value() == '960 ₽'

    def test_is_open_vkpay_iframe(self, budget_page):
        budget_page.click_replenish_budget_button()
        budget_page.enter_amount(budget_page.MIN_AMOUNT)
        budget_page.click_submit_button()
        assert budget_page.vkpay_iframe_became_visible()
