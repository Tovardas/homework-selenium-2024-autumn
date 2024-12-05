import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from ui.locators.create_campaign_page_locators import CreateCampaignPageLocators
from ui.pages.base_page import BasePage


class CreateCampaignPage(BasePage):
    url = 'https://ads.vk.com/hq/dashboard'
    locators = CreateCampaignPageLocators()

    def click_create_campaign_button(self):
        self.click(self.locators.CREATE_CAMPAIGN_BUTTON)

    def wait_for_redirect(self, expected_url_substring, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.url_contains(expected_url_substring))

    def select_site_option(self):
        self.click(self.locators.SITE_OPTION)

    def enter_advertised_site_url(self, url):
        site_field = self.find(self.locators.ADVERTISED_SITE_FIELD)
        site_field.clear()
        site_field.send_keys(url + Keys.RETURN)

    def is_element_displayed(self, locator):
        try:
            self.wait().until(EC.visibility_of_element_located(locator))
            return True
        except NoSuchElementException:
            return False

    def is_advertised_site_field_present(self):
        return self.is_element_displayed(self.locators.ADVERTISED_SITE_FIELD)

    def fields_displayed(self):
        return (
                self.is_element_displayed(self.locators.ADD_PIXEL) and
                self.is_element_displayed(self.locators.TARGET_ACTION) and
                self.is_element_displayed(self.locators.BETTING_STRATEGY) and
                self.is_element_displayed(self.locators.BUDGET) and
                self.is_element_displayed(self.locators.DATES)
        )

    def fill_budget_field(self, budget_value):
        budget_field = self.find(self.locators.BUDGET_INPUT)
        budget_field.clear()
        budget_field.send_keys(budget_value)

        budget_value_without_currency = budget_field.get_attribute("value").replace('₽', '')

        WebDriverWait(self.driver, 20).until(
            lambda driver: budget_value_without_currency in budget_field.get_attribute("value")
        )

    def click_continue_button(self):
        self.click(self.locators.CONTINUE_BUTTON)

    def select_region(self):
        self.click(self.locators.REGION)

    def click_cancel_button(self):
        self.click(self.locators.CANCEL_BUTTON)

    def click_save_as_draft_button(self):
        self.click(self.locators.SAVE_AS_DRAFT_BUTTON)

    def successful_save_displayed(self):
        return self.is_element_displayed(self.locators.SAVE_AS_DRAFT)
