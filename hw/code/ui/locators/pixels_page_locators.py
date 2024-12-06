from selenium.webdriver.common.by import By
from ui.locators.base_page_locators import BasePageLocators


class PixelsPageLocators(BasePageLocators):
    CREATE_PIXEL_BUTTON = (By.XPATH, '//span[@class="vkuiButton__content"]')
    PIXEL_MODAL_WINDOW = (By.XPATH, '//div[contains(@class, "vkuiInternalModalCardBase")]')
    PIXEL_ADD_BUTTON = (By.XPATH, '//div[contains(@class, "vkuiButtonGroup")]/button')
    PIXEL_DOMAIN_FIELD = (By.XPATH, '//input[@placeholder="Домен сайта"]')
    INCORRECT_PIXEL_ERROR = (By.XPATH, "//span[text()='Введите корректный адрес сайта (вида: example.ru)']")
    PIXEL_ID_MODAL_BUTTON = (By.XPATH, "//label[h4[text()='ID пикселя']]")
    MODAL_ID_PIXEL_FIELD = (By.XPATH, '//input[@placeholder="ID пикселя"]')
    MODAL_EMAIL_PIXEL_FIELD = (By.XPATH, '//input[@placeholder="Email владельца"]')
    INCORRECT_PIXEL_EMAIL_ERROR = (By.XPATH, "//span[@role='alert']//div[text()='Неверный email']")
    INCORRECT_PIXEL_EMAIL_REQUIRED_ERROR = (By.XPATH, "//span[@role='alert']//div[text()='Обязательное поле']")
    INCORRECT_PIXEL_ID_ERROR = (By.XPATH, "//span[@role='alert']//div[text()='Поле не может быть пустым']")
    MODAL_CREATE_NEW_PIXEL_CONF = (By.XPATH, "//div[@role='button' and .//span[text()='Создать новый пиксель']]")
    MODAL_CREATION_SUCCESS = (By.XPATH, "//h2[contains(text(), 'Создан ID пикселя')]")
    MODAL_CREATION_SUCCESS_CANCEL = (By.XPATH, "//div[@role='button' and @aria-label='Закрыть']")
    FIRST_ADDED_PIXEL_MORE = (By.XPATH, "(//button[@type='button' and @aria-label='More'])[last()]")
    PIXEL_DELETE_BUTTON = (By.XPATH, "//label[contains(., 'Удалить пиксель')]")
    PIXEL_DELETE_CONF = (By.XPATH, "//button[.//span[text()='Удалить']]")
    PIXEL_DELETE_CONF_CANCEL = (By.XPATH, "//button[.//span[text()='Отмена']]")
    PIXEL_RENAME_BUTTON = (By.XPATH, "//label[contains(., 'Переименовать')]")
    PIXEL_RENAME_CONF = (By.XPATH, "//button[.//span[text()='Изменить']]")
    PIXEL_RENAME_CONF_CANCEL = (By.XPATH, "//button[.//span[text()='Отмена']]")
    MODAL_RENAME_PIXEL_FIELD = (By.XPATH, '//input[@name="name"]')

    OPTIONS_BUTTON = (By.XPATH, "//a[contains(@href, '/hq/pixels/') and contains(@href, '/events')]")
    OPTIONS_CODE_PIXEL = (By.XPATH,
                          "//div[@id='tab_pixels.code' and @role='tab' and @aria-controls='pixels.code' and contains(@class, 'vkuiTabsItem') and contains(., 'Код пикселя')]")
    OPTIONS_TAGS = (
    By.XPATH, "//div[@role='tab' and @id='tab_pixels.audience_tags' and .//span[text()='Аудиторные теги']]")
    SWITCH_AUTO_SEARCH = (By.XPATH, "(//label[contains(@class, 'vkuiSwitch') and .//input[@type='checkbox']])[1]")
    SWITCH_DATA_LAYER = (By.XPATH, "(//label[contains(@class, 'vkuiSwitch') and .//input[@type='checkbox']])[2]")
    SWITCH_SYNC_USER = (By.XPATH, "(//label[contains(@class, 'vkuiSwitch') and .//input[@type='checkbox']])[3]")
    DATA_LAYER_FIELD = (By.XPATH,
                        "//input[@class='vkuiTypography vkuiInput__el vkuiText vkuiText--sizeY-compact' and @placeholder='Введите название слоя']")
    DATA_LAYER_WARNING = (By.XPATH,
                          "//span[@class='BaseCode_codeHighlight__HTidY' and text()='Убедитесь что на вашем сайте размещён код с правильным названием слоя данных']")
    USER_SYNC_WARNING = (By.XPATH,
                         "//div[@class='BaseCode_codeDescription__vxscq' and contains(text(), 'Настройте подмену шаблонного USER_ID на реальные данные при установке кода на сайт')]/div[@class='Hint_hintTrigger__ixYRu']")
    PIXEL_MAIN_BUTTON = (By.XPATH,
                         "//a[@href='/hq/pixels' and @data-route='pixels' and @data-testid='left-menu' and @data-entityid='pixels' and contains(., 'Сайты')]")

    CREATE_TAG_BUTTON = (
    By.XPATH, "//button[contains(@class, 'vkuiButton') and .//span[contains(., 'Создать аудиторный тег')]]")
    TAG_NAME_FIELD_ERROR = (By.XPATH,
                            "//span[contains(@class, 'vkuiTypography') and contains(@class, 'vkuiFormItem__bottom') and text()='Обязательное поле']")
    CREATE_TAG_CONF_FALSE = (
    By.XPATH, "//button[contains(@class, 'vkuiButton') and .//span[@class='vkuiButton__content' and text()='Отмена']]")
    CREATE_TAG_CONF_TRUE = (By.XPATH,
                            "//button[@type='submit' and contains(@class, 'vkuiButton') and .//span[@class='vkuiButton__content' and text()='Создать']]")
    TAG_NAME_FIELD = (By.XPATH,
                      "//input[contains(@class, 'vkuiTypography') and contains(@class, 'vkuiInput__el') and @placeholder='Введите название тега']")
    TAG_NAME_ELEMENT = (By.XPATH,
                        "//div[@role='gridcell' and @class='BaseTable__row-cell' and .//div[@class='BaseTable__row-cell-text' and text()='testing']]")

    NEW_EVENT_BUTTON = (By.XPATH,
                        "//button[contains(@class, 'vkuiButton') and contains(@class, 'vkuiButton--size-m') and contains(@class, 'vkuiButton--mode-primary') and .//span[text()='Добавить событие']]")
    RIGHT_SIDE_BAR = (By.XPATH, "//div[starts-with(@class, 'RightSidebar')]")
    NEW_EVENT_CONF_FALSE = (By.XPATH, "//button[@type='button' and @data-testid='cancel']")
    NEW_EVENT_CONF_TRUE = (By.XPATH, "//button[@type='submit' and @data-testid='submit']")
    EVENT_NAME_FIELD = (By.XPATH,
                        "//span[@class='vkuiFormField vkuiFormField--mode-default vkuiFormField--sizeY-compact vkui-focus-visible vkuiInput vkuiInput--sizeY-compact']/input[@type='text' and @placeholder='Введите название']")

    @staticmethod
    def CATEGORY_SELECT_INPUT(category):
        return (By.XPATH, f"//*[contains(@class, 'vkuiFormField') and .//*[text()='{category}']]//input")

    @staticmethod
    def DROPDOWN_OPTIONS(content):
        return (By.XPATH, f"(//*[text()='{content}'])[last()]")

    EVENT_CATEGORY_FIELD = (By.XPATH,
                            "//div[@class='vkuiCustomSelectInput__input-group']//input[@type='text' and @placeholder='Выберите категорию']")
    EVENT_CATEGORY_FIELD_CONTENT = (By.XPATH, "//select[@class='vkuiCustomSelect__control']/option[@value='purchase']")
    EVENT_REQUIREMENT_HREF = (By.XPATH,
                              "//div[@class='vkuiCustomSelect vkuiCustomSelect--sizeY-compact']//input[@placeholder='Выберите условие']")
    EVENT_REQUIREMENT_HREF_CONTENT = (By.XPATH, "//option[@value='uss']")
    EVENT_URL_FIELD = (By.XPATH, "//input[@placeholder='Введите значение']")
    EVENT_SET_VALUE_BUTTON = (By.XPATH,
                              "//button[@class='vkuiButton vkuiButton--size-m vkuiButton--mode-link vkuiButton--appearance-accent vkuiButton--align-center vkuiButton--with-icon vkuiTappable vkuiInternalTappable vkuiTappable--sizeX-none vkuiTappable--hasHover vkuiTappable--hasActive vkui-focus-visible']")
    EVENT_VALUE_FIELD = (By.XPATH,
                         "//input[@class='vkuiTypography vkuiInput__el vkuiText vkuiText--sizeY-compact' and @placeholder='Введите ценность']")

    EVENT_TIME_PERIOD_FIELD = (By.XPATH, "//div[@class='vkuiCustomSelect vkuiCustomSelect--sizeY-compact']")
    EVENT_AMOUNT_FIELD = (By.XPATH, "//input[@placeholder='Выберите количество']")
    EVENT_JS_FIELD = (By.XPATH, "(//input[@placeholder='Введите название'])[2]")
