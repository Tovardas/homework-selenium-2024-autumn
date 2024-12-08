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

    def add_custom_audience(self, audience_name):
        self.click(self.locators.ADD_CUSTOM_AUDIENCE)
        audience_field = self.find(self.locators.CUSTOM_AUDIENCE_INPUT)
        audience_field.clear()
        audience_field.send_keys(audience_name + Keys.RETURN)

    def get_audiences(self):
        return [elem.text for elem in self.find_elements(self.locators.AUDIENCE_LIST)]

    def duplicate_ad_group(self):
        self.click(self.locators.DUPLICATE_AD_GROUP)

    def get_last_ad_group_name(self):
        ad_group_names = [elem.text for elem in self.find_elements(self.locators.AD_GROUP_NAMES)]
        return ad_group_names[-1] if ad_group_names else None

    def add_ad_group(self, group_name):
        self.click(self.locators.ADD_AD_GROUP)
        group_field = self.find(self.locators.AD_GROUP_NAME_INPUT)
        group_field.clear()
        group_field.send_keys(group_name + Keys.RETURN)

    def remove_ad_group(self):
        self.click(self.locators.REMOVE_AD_GROUP_BUTTON)

    def get_ad_groups(self):
        return [elem.text for elem in self.find_elements(self.locators.AD_GROUP_NAMES)]

    def get_error_message(self):
        return self.find(self.locators.ERROR_MESSAGE).text

    def open_demographics_settings(self):
        self.click(self.locators.DEMOGRAPHICS_SETTINGS)

    def set_age_range(self, min_age, max_age):
        min_age_field = self.find(self.locators.MIN_AGE_INPUT)
        max_age_field = self.find(self.locators.MAX_AGE_INPUT)
        min_age_field.clear()
        max_age_field.clear()
        min_age_field.send_keys(min_age)
        max_age_field.send_keys(max_age)

    def open_company_creation(self):
        self.click(self.locators.CREATE_COMPANY_BUTTON)

    def set_site_url(self, site_url):
        site_field = self.find(self.locators.SITE_URL_INPUT)
        site_field.clear()
        site_field.send_keys(site_url)

    def open_catalogs_dropdown(self):
        self.click(self.locators.CATALOGS_DROPDOWN)

    def select_catalog(self, catalog_name):
        catalogs = self.find_elements(self.locators.CATALOG_LIST)
        for catalog in catalogs:
            if catalog.text == catalog_name:
                catalog.click()
                break

    def set_region(self):
        self.click(self.locators.REGION_SELECTOR)

    def apply_groups(self):
        self.click(self.locators.APPLY_GROUPS_BUTTON)

    def set_ad_header(self, header):
        header_field = self.find(self.locators.AD_HEADER_INPUT)
        header_field.clear()
        header_field.send_keys(header)

    def set_ad_short_desc(self, desc):
        desc_field = self.find(self.locators.AD_SHORT_DESC_INPUT)
        desc_field.clear()
        desc_field.send_keys(desc)

    def set_ad_carousel_desc(self, carousel_desc):
        carousel_field = self.find(self.locators.AD_CAROUSEL_DESC_INPUT)
        carousel_field.clear()
        carousel_field.send_keys(carousel_desc)

    def set_ad_card_desc(self, card_desc):
        card_field = self.find(self.locators.AD_CARD_DESC_INPUT)
        card_field.clear()
        card_field.send_keys(card_desc)

    def public_company(self):
        self.click(self.locators.PUBLIC_COMPANY_BUTTON)

    def wait_for_company_load(self, timeout=20):
        WebDriverWait(self.driver, timeout).until(
            lambda driver: "Клики по рекламе" in self.driver.page_source
        )
