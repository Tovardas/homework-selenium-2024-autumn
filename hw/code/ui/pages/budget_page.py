from ui.locators.budget_page_locators import BudgetPageLocators
from ui.pages.base_page import BasePage


class BudgetPage(BasePage):
    url = "https://ads.vk.com/hq/budget/transactions"
    locators = BudgetPageLocators()

    MIN_AMOUNT = 600
    MIN_AMOUNT_WITHOUT_VAT = 500
    MAX_AMOUNT = 200000
    MAX_AMOUNT_WITHOUT_VAT = 166666

    ERROR_TOO_LITTLE_AMOUNT = "Минимальная сумма 600,00 ₽"
    ERROR_TOO_LARGE_AMOUNT = "уменьшите сумму"

    def click_replenish_budget_button(self):
        self.click(self.locators.REPLENISH_BUDGET_BUTTON)

    def has_replenishment_modal_page_title(self):
        return self.became_visible(self.locators.REPLENISHMENT_MODAL_PAGE)

    def modal_has_h2_content_title(self):
        return self.became_visible(self.locators.MODAL_H2)

    def close_modal_page_became_visible(self):
        return self.became_visible(self.locators.CLOSE_MODAL_PAGE_BUTTON)

    def submit_button_became_visible(self):
        return self.became_visible(self.locators.SUBMIT_BUTTON)

    def inputs_became_visible(self):
        return self.became_visible(self.locators.AMOUNT_INPUT) and self.became_visible(
            self.locators.AMOUNT_WITHOUT_VAT_INPUT
        )

    def close_replenishment_modal_page(self):
        self.click(self.locators.CLOSE_MODAL_PAGE_BUTTON)

    def replenishment_modal_page_became_invisible(self) -> bool:
        return self.became_invisible(self.locators.REPLENISHMENT_MODAL_PAGE)

    def enter_amount(self, amount: str | int):
        amount_input = self.find(self.locators.AMOUNT_INPUT)
        amount_input.clear()
        amount_input.send_keys(amount)

    def get_amount_value(self) -> str | None:
        return self.find(self.locators.AMOUNT_INPUT).get_attribute("value")

    def enter_amount_without_vat(self, amount: str | int):
        amount_without_vat_input = self.find(self.locators.AMOUNT_WITHOUT_VAT_INPUT)
        amount_without_vat_input.clear()
        amount_without_vat_input.send_keys(amount)

    def get_amount_without_vat_value(self) -> str | None:
        return self.find(self.locators.AMOUNT_WITHOUT_VAT_INPUT).get_attribute("value")

    def get_error_message(self) -> str:
        return self.find(self.locators.ERROR_MESSAGE).text

    def click_submit_button(self):
        self.click(self.locators.SUBMIT_BUTTON)

    def vkpay_iframe_became_visible(self) -> bool:
        return self.became_visible(self.locators.VKPAY_IFRAME)
