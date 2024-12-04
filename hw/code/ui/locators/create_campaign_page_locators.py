from selenium.webdriver.common.by import By
from ui.locators.base_page_locators import BasePageLocators

class CreateCampaignPageLocators(BasePageLocators):
    CREATE_CAMPAIGN_BUTTON = (By.XPATH, '//button[@data-testid="create-button"]')
    LEARNING_MODAL_DISMISS_BUTTON = (By.XPATH, '//div[@role="button" and @aria-label="Закрыть"]')
    SITE_OPTION = (By.XPATH, '//div[@data-id="site_conversions"]')
    ADVERTISED_SITE_FIELD = (By.XPATH, '//input[@placeholder="Введите ссылку на сайт"]')

    ADD_PIXEL = (By.XPATH, "//span[text()='Добавить пиксель']")
    TARGET_ACTION = (By.XPATH, "//span[text()='Целевое действие']")
    BETTING_STRATEGY = (By.XPATH, "//span[text()='Стратегия ставок']")
    BUDGET = (By.XPATH, "//span[text()='Бюджет']")
    BUDGET_INPUT = (By.XPATH, '//input[@placeholder="Не задан"]')
    DATES = (By.XPATH, "//span[text()='Даты проведения']")

    REGION = (By.XPATH, "//span[text()='Россия']")

    CONTINUE_BUTTON = (
        By.XPATH, 
        "//button[@class='vkuiButton vkuiButton--size-l vkuiButton--mode-primary vkuiButton--appearance-accent vkuiButton--align-center vkuiButton--stretched vkuiTappable vkuiInternalTappable vkuiTappable--sizeX-none vkuiTappable--hasHover vkuiTappable--hasActive vkui-focus-visible']"
    )

    CANCEL_BUTTON = (
        By.XPATH,
        "//button[@class='vkuiButton vkuiButton--size-l vkuiButton--mode-secondary vkuiButton--appearance-accent vkuiButton--align-center vkuiButton--stretched vkuiTappable vkuiInternalTappable vkuiTappable--sizeX-none vkuiTappable--hasHover vkuiTappable--hasActive vkui-focus-visible']"
    )

    SAVE_AS_DRAFT_BUTTON = (
        By.XPATH, 
        "//button[contains(@class, 'vkuiButton--appearance-accent') and contains(@class, 'vkuiButton--mode-secondary') and contains(., 'Сохранить как черновик')]"
    )

    SAVE_AS_DRAFT = (
        By.XPATH, 
        "//div[contains(@class, 'CreateFooter_draftStatus__Hbe6f') and .//span[text()='Изменения сохранены']]"
    )
