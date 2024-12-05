import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from ui.pages.auth_page import AuthPage
from ui.pages.base_page import BasePage
from ui.pages.registration_page import RegistrationPage
from ui.pages.cabinet_page import CabinetPage
from ui.pages.settings_common_page import SettingsCommonPage
from ui.pages.settings_access_page import SettingsAccessPage
from ui.pages.settings_notifications_page import SettingsNotificationsPage
from ui.pages.pixels_page import PixelsPage
#from ui.pages.guide_page import GuidePage
from ui.pages.navbar_no_reg import NavbarNoReg
from ui.pages.guide_no_reg_page import GuideNoRegPage
from ui.pages.budget_page import BudgetPage
from ui.pages.center_commerce_page import CenterCommercePage
from ui.pages.audience_page import AudiencePage
from ui.pages.create_campaign_page import CreateCampaignPage
from ui.pages.forum_page import ForumsPage
from ui.pages.campaign_page import CampaignPage
from ui.verification.audience_verification import AudienceVerification
from ui.pages.cases_page import CasesPage

import os
from dotenv import load_dotenv


@pytest.fixture()
def driver(config):
    browser = config['browser']
    url = config['url']
    selenoid = config['selenoid']
    vnc = config['vnc']
    options = Options()
    if selenoid:
        capabilities = {
            'browserName': 'chrome',
            'version': '118.0',
        }
        if vnc:
            capabilities['enableVNC'] = True
        driver = webdriver.Remote(
            'http://127.0.0.1:4444/wd/hub',
            options=options,
        )
    elif browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    else:
        raise RuntimeError(f'Unsupported browser: "{browser}"')
    driver.get(url)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def base_page(driver):
    return BasePage(driver=driver)

@pytest.fixture(scope='session')
def credentials_with_cabinet():
    load_dotenv()
    return os.getenv('LOGIN'), os.getenv('PASSWORD')

@pytest.fixture
def auth_page(driver):
    return AuthPage(driver=driver)

@pytest.fixture
def cabinet_page(driver, credentials_with_cabinet, auth_page):
    driver.get(RegistrationPage.url)
    auth_page.login(*credentials_with_cabinet)
    return CabinetPage(driver=driver)

@pytest.fixture
def settings_common_page(driver, cabinet_page):
    driver.get(SettingsCommonPage.url)
    return SettingsCommonPage(driver=driver)

@pytest.fixture
def settings_access_page(driver, cabinet_page):
    driver.get(SettingsAccessPage.url)
    return SettingsAccessPage(driver=driver)

@pytest.fixture
def settings_notifications_page(driver, cabinet_page):
    driver.get(SettingsNotificationsPage.url)
    return SettingsNotificationsPage(driver=driver)

# @pytest.fixture
# def guide_page(driver, cabinet_page):
#     driver.get(GuidePage.url)
#     return GuidePage(driver=driver)

@pytest.fixture
def pixels_page(driver, cabinet_page):
    driver.get(PixelsPage.url)
    return PixelsPage(driver=driver)

@pytest.fixture
def navbar_no_reg(driver):
    return NavbarNoReg(driver=driver)

@pytest.fixture
def guide_no_reg_page(driver):
    return GuideNoRegPage(driver=driver)

@pytest.fixture
def forum_page(driver):
    driver.get(ForumsPage.url)
    return ForumsPage(driver=driver)

@pytest.fixture
def campaign_page(driver, cabinet_page):
    driver.get(CampaignPage.url)
    return CampaignPage(driver=driver)

@pytest.fixture
def center_commerce_page(driver, cabinet_page):
    driver.get(CenterCommercePage.url)
    return CenterCommercePage(driver=driver)

@pytest.fixture
def audience_page(driver, cabinet_page):
    driver.get(AudiencePage.url)
    return AudiencePage(driver=driver)

@pytest.fixture
def create_campaign_page(driver, cabinet_page):
    driver.get(CreateCampaignPage.url)
    return CreateCampaignPage(driver=driver)

@pytest.fixture
def budget_page(driver, cabinet_page):
    driver.get(BudgetPage.url)
    return BudgetPage(driver=driver)

@pytest.fixture
def verification(audience_page):
    return AudienceVerification(audience_page)

@pytest.fixture
def cases_page(driver):
    return CasesPage(driver=driver)
