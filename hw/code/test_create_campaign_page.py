import allure

from base_case import BaseCase


class TestCreateCampaignPage(BaseCase):
    def test_required_fields(self, create_campaign_page):
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
            assert current_url.startswith(expected_url)

    def test_cancel_button(self, create_campaign_page):
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
            assert current_url.startswith(expected_url)

    def test_invalid_url(self, create_campaign_page):
        with allure.step("Вводим некорректный URL и проверяем отображение ошибки"):
            create_campaign_page.click_create_campaign_button()
            create_campaign_page.select_site_option()
            invalid_url = 'invalid_url'
            create_campaign_page.enter_advertised_site_url(invalid_url)
            create_campaign_page.click_continue_button()
            error_message = create_campaign_page.get_error_message()
            assert error_message == "Не удалось подгрузить данные ссылки"

    def test_empty_budget_field(self, create_campaign_page):
        with allure.step("Оставляем поле бюджета пустым и проверяем отображение ошибки"):
            create_campaign_page.click_create_campaign_button()
            create_campaign_page.select_site_option()
            valid_url = 'https://education.vk.company/'
            create_campaign_page.enter_advertised_site_url(valid_url)
            create_campaign_page.click_continue_button()
            error_message = create_campaign_page.get_error_message()
            assert error_message == "Обязательное поле"

    def test_region_selection(self, create_campaign_page):
        with allure.step("Выбираем регионы показа и проверяем, что они добавлены"):
            create_campaign_page.click_create_campaign_button()
            create_campaign_page.select_site_option()
            create_campaign_page.select_region('Россия')
            selected_regions = create_campaign_page.get_selected_regions()
            assert 'Россия' in selected_regions, f"Регион 'Россия' не отображается среди выбранных: {selected_regions}"

    def test_custom_audience(self, create_campaign_page):
        with allure.step("Добавляем пользовательскую аудиторию и проверяем ее отображение"):
            create_campaign_page.click_create_campaign_button()
            create_campaign_page.select_site_option()
            create_campaign_page.add_custom_audience('Пользовательская аудитория 1')
            audience_list = create_campaign_page.get_audiences()
            assert 'Пользовательская аудитория 1' in audience_list, f"Пользовательская аудитория не добавлена: {audience_list}"

    def test_duplicate_ad_group(self, create_campaign_page):
        with allure.step("Дублируем группу объявлений и проверяем корректность копии"):
            create_campaign_page.click_create_campaign_button()
            create_campaign_page.select_site_option()
            valid_url = 'https://education.vk.company/'
            create_campaign_page.enter_advertised_site_url(valid_url)
            create_campaign_page.fill_budget_field('500')
            create_campaign_page.click_continue_button()
            create_campaign_page.select_region()
            create_campaign_page.click_continue_button()
            create_campaign_page.duplicate_ad_group()
            duplicated_group_name = create_campaign_page.get_last_ad_group_name()
            assert duplicated_group_name == "Копия группы объявлений"

    def test_remove_ad_group(self, create_campaign_page):
        with allure.step("Удаляем группу объявлений и проверяем, что группа исчезла"):
            create_campaign_page.click_create_campaign_button()
            create_campaign_page.select_site_option()
            valid_url = 'https://education.vk.company/'
            create_campaign_page.enter_advertised_site_url(valid_url)
            create_campaign_page.fill_budget_field('500')
            create_campaign_page.click_continue_button()
            create_campaign_page.select_region()
            create_campaign_page.click_continue_button()
            create_campaign_page.add_ad_group("Тестовая группа")
            create_campaign_page.remove_ad_group()
            groups = create_campaign_page.get_ad_groups()
            assert "Тестовая группа" not in groups

    def test_invalid_region(self, create_campaign_page):
        with allure.step("Вводим несуществующий регион и проверяем отображение ошибки"):
            create_campaign_page.click_create_campaign_button()
            create_campaign_page.select_site_option()
            valid_url = 'https://education.vk.company/'
            create_campaign_page.enter_advertised_site_url(valid_url)
            create_campaign_page.fill_budget_field('500')
            create_campaign_page.click_continue_button()
            create_campaign_page.enter_region("Несуществующий регион")
            error_message = create_campaign_page.get_error_message()
            assert error_message == "Ничего не нашлось"

    def test_empty_logo(self, create_campaign_page):
        with allure.step("Не загружаем логотип и проверяем отображение ошибки"):
            create_campaign_page.click_create_campaign_button()
            create_campaign_page.select_site_option()
            valid_url = 'https://education.vk.company/'
            create_campaign_page.enter_advertised_site_url(valid_url)
            create_campaign_page.fill_budget_field('500')
            create_campaign_page.click_continue_button()
            create_campaign_page.select_region()
            create_campaign_page.click_continue_button()
            create_campaign_page.enter_ad_details(title="Тест", description="Тест описание")
            create_campaign_page.click_publish_button()
            error_message = create_campaign_page.get_error_message()
            assert error_message == "Логотип обязателен"

    def test_invalid_age_order(self, create_campaign_page):
        with allure.step("Устанавливаем минимальный возраст больше максимального и проверяем ошибку"):
            create_campaign_page.click_create_campaign_button()
            create_campaign_page.select_site_option()
            create_campaign_page.open_demographics_settings()
            create_campaign_page.set_age_range(min_age="50", max_age="30")
            error_message = create_campaign_page.get_error_message()
            assert error_message == "Минимальный возраст не может быть больше максимального"

    def test_create_catalog_company(self, create_campaign_page):
        create_campaign_page.open_company_creation()
        assert "Сайт" in create_campaign_page.driver.page_source
        site_url = 'https://education.vk.company/'
        create_campaign_page.set_site_url(site_url)
        assert site_url in create_campaign_page.driver.page_source
        create_campaign_page.open_catalogs_dropdown()
        create_campaign_page.select_catalog("Каталог 2024-12-08")
        assert 'Целевое действие' in create_campaign_page.driver.page_source
        assert 'Стратегия ставок' in create_campaign_page.driver.page_source
        assert 'Бюджет' in create_campaign_page.driver.page_source
        assert 'Дата проведения' in create_campaign_page.driver.page_source
        create_campaign_page.set_region()
        assert 'Россия' in create_campaign_page.driver.page_source
        create_campaign_page.apply_groups()

        ad_header = 'AD'
        ad_desc = 'DESC'
        ad_carousel = 'CAROUSEL'
        ad_card = 'CARD'

        create_campaign_page.set_ad_header(ad_header)
        create_campaign_page.set_ad_short_desc(ad_desc)
        create_campaign_page.set_ad_carousel_desc(ad_carousel)
        create_campaign_page.set_ad_card_desc(ad_card)
        assert ad_header in create_campaign_page.driver.page_source
        assert ad_desc in create_campaign_page.driver.page_source
        assert ad_carousel in create_campaign_page.driver.page_source

        create_campaign_page.public_company()
        create_campaign_page.wait_for_company_load()

        assert 'Клики по рекламе' in create_campaign_page.driver.page_source
        assert 'Каталог товаров' in create_campaign_page.driver.page_source

    def test_create_public_company(self, create_campaign_page):
        create_campaign_page.open_company_creation()
        assert "Рекламируемый объект" in create_campaign_page.driver.page_source
        site_url = 'Артемий Лебедев'
        create_campaign_page.set_site_url(site_url)
        assert site_url in create_campaign_page.driver.page_source
        assert 'Целевое действие' in create_campaign_page.driver.page_source
        assert 'Стратегия ставок' in create_campaign_page.driver.page_source
        assert 'Бюджет' in create_campaign_page.driver.page_source
        assert 'Дата проведения' in create_campaign_page.driver.page_source

        create_campaign_page.set_region()
        assert 'Россия' in create_campaign_page.driver.page_source

        create_campaign_page.apply_groups()

        ad_header = 'AD'
        ad_desc = 'DESC'

        create_campaign_page.set_ad_header(ad_header)
        create_campaign_page.set_ad_short_desc(ad_desc)
        assert ad_header in create_campaign_page.driver.page_source
        assert ad_desc in create_campaign_page.driver.page_source
        create_campaign_page.public_company()
        create_campaign_page.wait_for_company_load()

        assert 'Подписка на сообщество' in create_campaign_page.driver.page_source
        assert 'Сообщество ВКонтакте' in create_campaign_page.driver.page_source
