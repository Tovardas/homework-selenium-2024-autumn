import allure

from base_case import BaseCase


class TestCampaignPage(BaseCase):

    @allure.title("Тест процесса создания кампании")
    def test_campaign_group_ad_created(self, campaign_page, campaign_verification):
        with allure.step("Нажимаем кнопку 'Создать' и проверяем поток создания"):
            campaign_page.click_create_button()
            campaign_verification.check_create_button_flow()

        with allure.step("Нажимаем на вкладки распознавания и проверяем содержимое"):
            campaign_page.click_recognition_tabs()
            campaign_verification.check_recognition_tabs()

        with allure.step("Нажимаем на вкладки целей, выбираем сайт и проверяем поля ввода"):
            campaign_page.click_target_tabs()
            campaign_page.click_site_cell()
            campaign_verification.check_site_inputs()

        with allure.step("Заполняем название сайта и проверяем создание кампании"):
            campaign_page.fill_site_name_with_valid_url()
            campaign_page.click_target_tabs()
            campaign_verification.check_campaign_created()

        with allure.step("Переименовываем кампанию и заполняем форму перед нажатием на 'Продолжить'"):
            campaign_page.rename_entity(campaign_page.CAMPAIGN_NAME)
            campaign_page.fill_campaign_form()
            campaign_page.click_continue_button()
            campaign_verification.check_group_creation_url()
            assert self.is_opened(
                r"https://ads\.vk\.com/hq/new_create/ad_plan/new-site_conversions/ad_group/new-ad-group-form_\d+")

        with allure.step("Переименовываем группу и проверяем раздел регионов"):
            campaign_page.rename_entity(campaign_page.GROUP_NAME)
            campaign_verification.check_region_section()

        with allure.step("Выбираем Россию, проверяем раздел демографии и заполняем его"):
            campaign_page.click_russia_button()
            campaign_page.click_demography_section()
            campaign_verification.check_demography_section()

        with allure.step("Заполняем данные демографии, переходим в раздел интересов и проверяем видимость"):
            campaign_page.fill_demography()
            campaign_page.click_demography_section()
            campaign_page.click_interest_section()
            campaign_verification.check_interest_subsection_visibility()

        with allure.step("Нажимаем на подраздел интересов и проверяем его содержимое"):
            campaign_page.click_interest_subsection()
            campaign_verification.check_interest_subsection_content()

        with allure.step("Заполняем интересы, открываем раздел 'Остановить интерес' и заполняем его"):
            campaign_page.fill_interests()
            campaign_page.click_stop_interest_opener()
            campaign_page.has_stop_interest_content()
            campaign_page.fill_stop_interest()
            campaign_page.click_interest_section()
            campaign_page.click_device_section()
            campaign_verification.check_device_section()

        with allure.step(
                "Нажимаем на чекбокс мобильных устройств и на кнопку 'Продолжить', проверяем URL формы объявления"):
            campaign_page.click_mobile_checkbox()
            campaign_page.click_continue_button()
            assert self.is_opened(
                r"https://ads\.vk\.com/hq/new_create/ad_plan/new-site_conversions/ad_group/new-ad-group-form_\d+/ad/new-ad-form_\d+")
            campaign_verification.check_ad_fields()

        with allure.step("Переименовываем объявление и проверяем содержимое боковой панели с медиа"):
            campaign_page.rename_entity(campaign_page.AD_NAME)
            campaign_page.click_logo_input()
            campaign_verification.check_media_sidebar_content()

        with allure.step("Выбираем изображение и проверяем видимость превью"):
            campaign_page.click_image_item()
            campaign_verification.check_preview_image_visibility()

        with allure.step("Заполняем данные объявления, проверяем медиа-контент и видимость кнопок"):
            campaign_page.fill_ad_inputs_and_textarea()
            campaign_page.click_media()
            campaign_page.has_mediatec_sidebar_image_content()
            campaign_page.click_image_item()
            campaign_page.submit_button_became_visible()
            campaign_page.click_submit_button()
            campaign_verification.check_media_content_and_buttons()

        with allure.step("Нажимаем на кнопку 'Опубликовать' и проверяем содержимое модального окна с ошибкой"):
            campaign_page.click_publish_button()
            campaign_verification.check_bug_modal_content()

        with allure.step("Нажимаем на кнопку 'Отправить отчет об ошибке' и проверяем состояние страницы кампании"):
            campaign_page.click_send_bug_modal()
            assert self.is_opened('https://ads.vk.com/hq/dashboard/ad_plans')
            campaign_verification.check_campaign_page_state()

        with allure.step("Наводим курсор на название кампании и проверяем видимость кнопки редактирования"):
            campaign_page.hover_campaign_title()
            campaign_verification.check_edit_button_visibility()

        with allure.step("Нажимаем на 'Редактировать' и проверяем значения в форме кампании"):
            campaign_page.click_edit()
            campaign_verification.check_campaign_form_values()

        with allure.step("Отменяем изменения в форме кампании и проверяем состояние группы после отмены"):
            campaign_page.click_cancel_button()
            campaign_page.click_confirm_cancel_button()
            campaign_page.click_group_tabs()
            campaign_verification.check_group_state_after_cancel()

        with allure.step("Наводим курсор на название группы и проверяем видимость кнопки редактирования"):
            campaign_page.hover_group_title()
            campaign_verification.check_group_edit_button_visibility()

        with allure.step("Нажимаем на 'Редактировать' и проверяем значения в форме группы"):
            campaign_page.click_edit()
            campaign_verification.check_group_form_values()

        with allure.step("Отменяем изменения в форме группы и проверяем состояние объявления после отмены"):
            campaign_page.click_cancel_button()
            campaign_page.click_confirm_cancel_button()
            campaign_page.click_ad_tab()
            campaign_verification.check_ad_state_after_cancel()

        with allure.step("Наводим курсор на название объявления и проверяем видимость кнопки редактирования"):
            campaign_page.hover_ad_title()
            campaign_verification.check_ad_edit_button_visibility()

        with allure.step("Нажимаем на 'Редактировать' и проверяем значения в форме объявления"):
            campaign_page.click_edit()
            campaign_verification.check_ad_edit_form_values()

        with allure.step("Отменяем изменения в форме объявления и удаляем сущность"):
            campaign_page.click_cancel_button()
            campaign_page.click_confirm_cancel_button()
            campaign_page.delete_entity()
