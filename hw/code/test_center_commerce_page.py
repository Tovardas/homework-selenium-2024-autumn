from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from base_case import BaseCase


class TestCommerceCenter(BaseCase):
    def test_open_catalog_modal(self, center_commerce_page):
        center_commerce_page.close_training_modal()
        center_commerce_page.click_create_catalog_button()
        WebDriverWait(center_commerce_page.driver, 10).until(
            EC.invisibility_of_element_located(center_commerce_page.locators.CATALOG_MODAL_PAGE)
        )
        assert center_commerce_page.catalog_modal_page_became_visible(), "Модальное окно создания каталога не открылось"

    def test_click_catalog_modal_cancel_button(self, center_commerce_page):
        center_commerce_page.close_training_modal()
        center_commerce_page.click_create_catalog_button()
        center_commerce_page.cancel_catalog_button()
        WebDriverWait(center_commerce_page.driver, 10).until(
            EC.invisibility_of_element_located(center_commerce_page.locators.CATALOG_MODAL_PAGE)
        )
        assert not center_commerce_page.catalog_modal_page_became_visible(), "Модальное окно создания каталога должно быть закрыто после нажатия кнопки 'Отмена'"

    def test_click_catalog_modal_close_button(self, center_commerce_page):
        center_commerce_page.close_training_modal()
        center_commerce_page.click_create_catalog_button()
        center_commerce_page.close_catalog_button()
        WebDriverWait(center_commerce_page.driver, 10).until(
            EC.invisibility_of_element_located(center_commerce_page.locators.CATALOG_MODAL_PAGE)
        )

        assert not center_commerce_page.catalog_modal_page_became_visible(), "Модальное окно создания каталога должно быть закрыто после нажатия кнопки 'Закрыть'"

    def test_open_choice_learning_modal(self, center_commerce_page):
        center_commerce_page.close_training_modal()
        center_commerce_page.сlick_choice_learning()
        assert center_commerce_page.choice_learning_modal_page_became_visible(), "Модальное окно создания каталога не открылось"

    def test_close_choice_learning_modal(self, center_commerce_page):
        center_commerce_page.close_training_modal()
        center_commerce_page.сlick_choice_learning()
        WebDriverWait(center_commerce_page.driver, 10).until(
            EC.invisibility_of_element_located(center_commerce_page.locators.CHOICE_LEARNING_MODAL)
        )

        assert center_commerce_page.close_choice_learning_modal_page(), "Модальное окно создания каталога не закрылось"

    def test_empty_catalog_name_error(self, center_commerce_page):
        center_commerce_page.close_training_modal()
        center_commerce_page.click_create_catalog_button()
        center_commerce_page.input_empty_catalog_name()
        center_commerce_page.click_submit_button()

        assert center_commerce_page.is_required_field_error_displayed(), "Ошибка 'Обязательное поле' не отображается"

    def test_create_catalog_with_feed(self, center_commerce_page):
        center_commerce_page.close_training_modal()
        center_commerce_page.click_create_catalog_button()
        center_commerce_page.select_feed_or_community()

        assert center_commerce_page.field_feed_displayed(), "Поле 'Ссылка на фид или сообщество' не найдено"
        assert center_commerce_page.field_period_displayed(), "Поле 'Период обновления' не найдено"
        assert center_commerce_page.field_utm_displayed(), "Поле 'Автоматически удалять UTM-метки' не найдено"

    def test_create_catalog_with_marketplace(self, center_commerce_page):
        center_commerce_page.close_training_modal()
        center_commerce_page.click_create_catalog_button()
        center_commerce_page.select_marketplace()

        assert center_commerce_page.verify_marketplace_fields_visible(), "Поле 'Ссылка на страницу продавца' не найдено"

    def test_create_catalog_manually(self, center_commerce_page):
        center_commerce_page.close_training_modal()
        center_commerce_page.click_create_catalog_button()
        center_commerce_page.select_manually()

        assert center_commerce_page.field_category_displayed(), "Поле 'Категория фида' не найдено"
        assert center_commerce_page.field_feed_file_displayed(), "Поле 'Файл фида' не найдено"
        assert center_commerce_page.field_utm_displayed(), "Поле 'Автоматически удалять UTM-метки' не найдено"

    def test_empty_feed_url(self, center_commerce_page):
        center_commerce_page.close_training_modal()
        center_commerce_page.click_create_catalog_button()
        center_commerce_page.select_feed_or_community()
        center_commerce_page.click_submit_button()

        assert center_commerce_page.is_required_field_error_displayed(), "Ошибка 'Обязательное поле' не отображается"

    def test_invalid_feed_url(self, center_commerce_page):
        center_commerce_page.close_training_modal()
        center_commerce_page.click_create_catalog_button()
        center_commerce_page.select_feed_or_community()
        center_commerce_page.input_invalid_feed_url()
        center_commerce_page.click_submit_button()

        assert center_commerce_page.is_required_field_error_displayed(), "Ошибка 'Необходимо указать протокол http(s)' не отображается"

    def test_empty_marketplace_url(self, center_commerce_page):
        center_commerce_page.close_training_modal()
        center_commerce_page.click_create_catalog_button()
        center_commerce_page.select_marketplace()
        center_commerce_page.click_submit_button()

        assert center_commerce_page.is_required_field_error_displayed(), "Ошибка 'Обязательное поле' не отображается"

    def test_invalid_marketplace_url(self, center_commerce_page):
        center_commerce_page.close_training_modal()
        center_commerce_page.click_create_catalog_button()
        center_commerce_page.select_marketplace()
        center_commerce_page.input_invalid_marketplace_url()
        center_commerce_page.click_submit_button()

        assert center_commerce_page.is_required_field_error_displayed(), "Ошибка 'Необходимо указать протокол http(s)' не отображается"
