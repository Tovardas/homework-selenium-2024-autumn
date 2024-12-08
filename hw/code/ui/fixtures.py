import os

import pytest
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from ui.pages.audience_page import AudiencePage
from ui.pages.auth_page import AuthPage
from ui.pages.base_page import BasePage
from ui.pages.cabinet_page import CabinetPage
from ui.pages.campaign_page import CampaignPage
from ui.pages.create_campaign_page import CreateCampaignPage
from ui.pages.lead_forms_page import LeadFormsPage
from ui.pages.surveys_page import SurveysPage
from ui.pages.registration_page import RegistrationPage
from ui.pages.settings_common_page import SettingsCommonPage

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
def campaign_page(driver, cabinet_page):
    driver.get(CampaignPage.url)
    return CampaignPage(driver=driver)



@pytest.fixture
def audience_page(driver, cabinet_page):
    driver.get(AudiencePage.url)
    return AudiencePage(driver=driver)


@pytest.fixture
def create_campaign_page(driver, cabinet_page):
    driver.get(CreateCampaignPage.url)
    return CreateCampaignPage(driver=driver)


@pytest.fixture
def surveys_page(driver, cabinet_page):
    driver.get(SurveysPage.url)
    return SurveysPage(driver=driver)



@pytest.fixture
def leadforms_page(driver, cabinet_page):
    driver.get(LeadFormsPage.url)
    return LeadFormsPage(driver=driver)
