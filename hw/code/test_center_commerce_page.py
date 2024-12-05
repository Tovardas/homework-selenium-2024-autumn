import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from base_case import BaseCase


class TestCommerceCenter(BaseCase):

    @allure.title("Открытие модального окна создания каталога")
    def test_open_catalog_modal(self, center_commerce_page, commerce_center_verification):
        with allure.step(
                "Закрываем обучающее модальное окно, нажимаем 'Создать каталог' и проверяем открытие модального окна"):
            center_commerce_page.close_training_modal()
            center_commerce_page.click_create_catalog_button()
            WebDriverWait(center_commerce_page.driver, 10).until(
                EC.invisibility_of_element_located(center_commerce_page.locators.CATALOG_MODAL_PAGE)
            )
            commerce_center_verification.check_catalog_modal_visibility()

    @allure.title("Отмена создания каталога через кнопку 'Отмена'")
    def test_click_catalog_modal_cancel_button(self, center_commerce_page, commerce_center_verification):
        with allure.step(
                "Закрываем обучающее модальное окно, нажимаем 'Создать каталог', затем 'Отмена', проверяем закрытие окна"):
            center_commerce_page.close_training_modal()
            center_commerce_page.click_create_catalog_button()
            center_commerce_page.cancel_catalog_button()
            WebDriverWait(center_commerce_page.driver, 10).until(
                EC.invisibility_of_element_located(center_commerce_page.locators.CATALOG_MODAL_PAGE)
            )
            commerce_center_verification.check_catalog_modal_invisibility()

        with allure.step(
                "Закрываем обучающее модальное окно, нажимаем 'Создать каталог', затем крестик, проверяем закрытие окна"):
            center_commerce_page.close_training_modal()
            center_commerce_page.click_create_catalog_button()
            center_commerce_page.close_catalog_button()
            WebDriverWait(center_commerce_page.driver, 10).until(
                EC.invisibility_of_element_located(center_commerce_page.locators.CATALOG_MODAL_PAGE)
            )
            commerce_center_verification.check_catalog_modal_invisibility()

    @allure.title("Открытие модального окна обучения")
    def test_open_choice_learning_modal(self, center_commerce_page, commerce_center_verification):
        with allure.step(
                "Закрываем обучающее модальное окно, нажимаем кнопку выбора обучения и проверяем открытие модального окна"):
            center_commerce_page.close_training_modal()
            center_commerce_page.сlick_choice_learning()
            commerce_center_verification.check_choice_learning_modal_visibility()

    @allure.title("Закрытие модального окна обучения")
    def test_close_choice_learning_modal(self, center_commerce_page, commerce_center_verification):
        with allure.step(
                "Закрываем обучающее модальное окно, открываем модальное окно обучения, закрываем его и проверяем закрытие"):
            center_commerce_page.close_training_modal()
            center_commerce_page.сlick_choice_learning()
            WebDriverWait(center_commerce_page.driver, 10).until(
                EC.invisibility_of_element_located(center_commerce_page.locators.CHOICE_LEARNING_MODAL)
            )
            commerce_center_verification.check_choice_learning_modal_close()

    @allure.title("Проверка ошибки при пустом имени каталога")
    def test_empty_catalog_name_error(self, center_commerce_page, commerce_center_verification):
        with allure.step(
                "Закрываем обучающее модальное окно, нажимаем 'Создать каталог', оставляем имя пустым, проверяем ошибку"):
            center_commerce_page.close_training_modal()
            center_commerce_page.click_create_catalog_button()
            center_commerce_page.input_empty_catalog_name()
            center_commerce_page.click_submit_button()
            commerce_center_verification.check_required_field_error()

    @allure.title("Создание каталога с использованием фида")
    def test_create_catalog_with_feed(self, center_commerce_page, commerce_center_verification):
        with allure.step(
                "Закрываем обучающее модальное окно, нажимаем 'Создать каталог', выбираем фид, проверяем отображение полей"):
            center_commerce_page.close_training_modal()
            center_commerce_page.click_create_catalog_button()
            center_commerce_page.select_feed_or_community()
            commerce_center_verification.check_feed_fields()

    @allure.title("Создание каталога с использованием маркетплейса")
    def test_create_catalog_with_marketplace(self, center_commerce_page, commerce_center_verification):
        with allure.step(
                "Закрываем обучающее модальное окно, нажимаем 'Создать каталог', выбираем маркетплейс, проверяем отображение полей"):
            center_commerce_page.close_training_modal()
            center_commerce_page.click_create_catalog_button()
            center_commerce_page.select_marketplace()
            commerce_center_verification.check_marketplace_fields()

    @allure.title("Создание каталога вручную")
    def test_create_catalog_manually(self, center_commerce_page, commerce_center_verification):
        with allure.step(
                "Закрываем обучающее модальное окно, нажимаем 'Создать каталог', выбираем ручное создание, проверяем отображение полей"):
            center_commerce_page.close_training_modal()
            center_commerce_page.click_create_catalog_button()
            center_commerce_page.select_manually()
            commerce_center_verification.check_manual_fields()

    @allure.title("Проверка ошибки при пустом URL фида")
    def test_empty_feed_url(self, center_commerce_page, commerce_center_verification):
        with allure.step(
                "Закрываем обучающее модальное окно, нажимаем 'Создать каталог', выбираем фид, оставляем URL пустым, проверяем ошибку"):
            center_commerce_page.close_training_modal()
            center_commerce_page.click_create_catalog_button()
            center_commerce_page.select_feed_or_community()
            center_commerce_page.click_submit_button()
            commerce_center_verification.check_required_field_error()

    @allure.title("Проверка ошибки при неверном URL фида")
    def test_invalid_feed_url(self, center_commerce_page, commerce_center_verification):
        with allure.step(
                "Закрываем обучающее модальное окно, нажимаем 'Создать каталог', выбираем фид, вводим неверный URL, проверяем ошибку"):
            center_commerce_page.close_training_modal()
            center_commerce_page.click_create_catalog_button()
            center_commerce_page.select_feed_or_community()
            center_commerce_page.input_invalid_feed_url()
            center_commerce_page.click_submit_button()
            commerce_center_verification.check_required_field_error()

    @allure.title("Проверка ошибки при пустом URL маркетплейса")
    def test_empty_marketplace_url(self, center_commerce_page, commerce_center_verification):
        with allure.step(
                "Закрываем обучающее модальное окно, нажимаем 'Создать каталог', выбираем маркетплейс, оставляем URL пустым, проверяем ошибку"):
            center_commerce_page.close_training_modal()
            center_commerce_page.click_create_catalog_button()
            center_commerce_page.select_marketplace()
            center_commerce_page.click_submit_button()
            commerce_center_verification.check_required_field_error()

    @allure.title("Проверка ошибки при неверном URL маркетплейса")
    def test_invalid_marketplace_url(self, center_commerce_page, commerce_center_verification):
        with allure.step(
                "Закрываем обучающее модальное окно, нажимаем 'Создать каталог', выбираем маркетплейс, вводим неверный URL, проверяем ошибку"):
            center_commerce_page.close_training_modal()
            center_commerce_page.click_create_catalog_button()
            center_commerce_page.select_marketplace()
            center_commerce_page.input_invalid_marketplace_url()
            center_commerce_page.click_submit_button()
            commerce_center_verification.check_required_field_error()
