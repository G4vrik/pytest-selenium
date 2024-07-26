# import pytest
# from selenium import webdriver
# from selenium.webdriver.firefox.service import Service
# from webdriver_manager.firefox import GeckoDriverManager

# @pytest.fixture
# def driver(request):
#     service = Service(GeckoDriverManager().install())
#     driver = webdriver.Firefox(service=service)
#     driver.maximize_window()
#     request.addfinalizer(driver.quit)
#     return driver

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver(request):
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    request.addfinalizer(driver.quit)
    return driver