import pytest

from ui.pages.base_page import PageNotOpenedException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urllib.parse import urlparse, parse_qs


class BaseCase:
    def is_opened(self, url, timeout=None):
        if timeout is None:
            timeout = 5

        try:
            WebDriverWait(self.driver, timeout).until(EC.url_matches(url))
            return True
        except:
            raise PageNotOpenedException(
                f'{url} did not open in {timeout} sec, current url {self.driver.current_url}')

    def query_parameter_matches(self, parameter, value, timeout=None):
        if timeout is None:
            timeout = 5

        def parameters_match(driver):
            current_url = driver.current_url
            parsed_url = urlparse(current_url)
            query_params = parse_qs(parsed_url.query)
            expected_params = {parameter: [str(value)]}
            return query_params == expected_params

        try:
            WebDriverWait(self.driver, timeout).until(parameters_match)
            return True
        except:
            raise PageNotOpenedException(
                f"Не удалось найти параметр '{parameter}={value}' в URL за {timeout} секунд. Текущий URL: {self.driver.current_url}"
            )