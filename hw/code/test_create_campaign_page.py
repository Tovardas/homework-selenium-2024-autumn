import allure

from base_case import BaseCase


class TestCreateCampaignPage(BaseCase):
    def test_open_catalog_modal(self, create_campaign_page, create_campaign_page_verification):
        with allure.step("Нажимаем кнопку создания кампании и проверяем редирект на страницу создания кампании"):
            create_campaign_page.click_create_campaign_button()
            expected_url = 'https://ads.vk.com/hq/new_create/ad_plan'
            create_campaign_page.wait_for_redirect(expected_url)
            current_url = create_campaign_page.driver.current_url
            create_campaign_page_verification.check_url(current_url, expected_url)

    def test_site_option_displays_advertised_site_field(self, create_campaign_page, create_campaign_page_verification):
        with allure.step(
                "Нажимаем кнопку создания кампании и проверяем, что поле для ввода рекламируемого сайта отображается после выбора опции сайта"):
            create_campaign_page.click_create_campaign_button()
            create_campaign_page.select_site_option()
            create_campaign_page_verification.check_advertised_site_field_present()

    def test_valid_url_site_input(self, create_campaign_page, create_campaign_page_verification):
        with allure.step("Вводим правильный URL в поле рекламируемого сайта и проверяем отображение полей"):
            create_campaign_page.click_create_campaign_button()
            create_campaign_page.select_site_option()
            valid_url = 'https://education.vk.company/'
            create_campaign_page.enter_advertised_site_url(valid_url)
            create_campaign_page_verification.check_fields_displayed()

    def test_required_fields(self, create_campaign_page, create_campaign_page_verification):
        with allure.step("Заполняем обязательные поля и проверяем редирект на следующий шаг"):
            create_campaign_page.click_create_campaign_button()
            create_campaign_page.select_site_option()
            valid_url = 'https://education.vk.company/'
            create_campaign_page.enter_advertised_site_url(valid_url)
            create_campaign_page.fill_budget_field('500')
            create_campaign_page.click_continue_button()
            expected_url = 'https://ads.vk.com/hq/new_create/ad_plan/new-site_conversions/ad_group/new-ad-group-form_'
            create_campaign_page.wait_for_redirect(expected_url)
            current_url = create_campaign_page.driver.current_url
            create_campaign_page_verification.check_url_startswith(current_url, expected_url)

    def test_ads_required_fields(self, create_campaign_page, campaign_verification):
        with allure.step("Заполняем обязательные поля для объявления и переходим к следующему шагу"):
            create_campaign_page.click_create_campaign_button()
            create_campaign_page.select_site_option()
            valid_url = 'https://education.vk.company/'
            create_campaign_page.enter_advertised_site_url(valid_url)
            create_campaign_page.fill_budget_field('500')
            create_campaign_page.click_continue_button()
            create_campaign_page.select_region()
            create_campaign_page.click_continue_button()
            campaign_verification.check_ad_fields()

    def test_cancel_button(self, create_campaign_page, create_campaign_page_verification):
        with allure.step("Нажимаем кнопку отмены и проверяем редирект на страницу формы создания группы кампании"):
            create_campaign_page.click_create_campaign_button()
            create_campaign_page.select_site_option()
            valid_url = 'https://education.vk.company/'
            create_campaign_page.enter_advertised_site_url(valid_url)
            create_campaign_page.fill_budget_field('500')
            create_campaign_page.click_continue_button()
            create_campaign_page.select_region()
            create_campaign_page.click_continue_button()
            create_campaign_page.click_cancel_button()
            expected_url = 'https://ads.vk.com/hq/new_create/ad_plan/new-site_conversions/ad_group/new-ad-group-form_'
            create_campaign_page.wait_for_redirect(expected_url)
            current_url = create_campaign_page.driver.current_url
            create_campaign_page_verification.check_url_startswith(current_url, expected_url)
