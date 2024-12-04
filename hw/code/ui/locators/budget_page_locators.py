from selenium.webdriver.common.by import By
from ui.locators.base_page_locators import BasePageLocators


class BudgetPageLocators(BasePageLocators):
    REPLENISH_BUDGET_BUTTON = (
        By.XPATH,
        "//*[contains(@class, 'vkuiButton__content') and text()='Пополнить счёт']",
    )
    REPLENISHMENT_MODAL_PAGE = (By.XPATH, "//*[contains(@id, '_modal_')]")

    CLOSE_MODAL_PAGE_BUTTON = (
        By.XPATH,
        "//*[contains(@class, 'vkuiModalDismissButton')]",
    )

    MODAL_H2 = (
        By.XPATH,
        "//*[contains(@class, 'vkuiTitle--level-3') and text()='Пополнение счёта']",
    )

    AMOUNT_INPUT = (By.NAME, "amount")
    AMOUNT_WITHOUT_VAT_INPUT = (By.NAME, "amountWithoutVat")

    ERROR_MESSAGE = (By.XPATH, "//*[@role='alert']")

    SUBMIT_BUTTON = (By.XPATH, "//*[contains(@class, 'CreateInvoiceModal_button__')]")

    VKPAY_IFRAME = (By.XPATH, "//iframe[contains(@class, 'CreateInvoiceModal_iframe')]")
