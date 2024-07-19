# import pytest
# from selenium import webdriver
# from selenium.webdriver.firefox.service import Service
# from webdriver_manager.firefox import GeckoDriverManager


# @pytest.fixture(scope="function", autouse=True)
# def browser():
#     service = Service(GeckoDriverManager().install())
#     driver = webdriver.Firefox(service=service)
#     driver.maximize_window()
#     yield driver
#     # driver.quit()

import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

@pytest.fixture
def driver(request):
    service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)
    driver.maximize_window()
    request.addfinalizer(driver.quit)
    return driver

# 1) Переработать расположение классов и файлов
# 2) Отказаться от By
# 3) Добавить allure