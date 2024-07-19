import pytest
from config.data import Data
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.clients_page import ClientsPage


class BaseTest:

    data: Data
    login_page: LoginPage
    main_page: MainPage
    clients_page: ClientsPage

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.data = Data()
        request.cls.login_page = LoginPage(driver)
        request.cls.main_page = MainPage(driver)
        request.cls.clients_page = ClientsPage(driver)