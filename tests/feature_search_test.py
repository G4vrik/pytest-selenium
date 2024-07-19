import allure
import pytest
from base.base_test import BaseTest


@allure.feature("Проверка поиска")
class TestSearch(BaseTest):

    @allure.title("Проверка поиска xtnj")
    @allure.severity("critical")
    @pytest.mark.smoke
    def test_search(self):
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_submit_button()
        self.main_page.is_opened_main()
        self.main_page.click_clients()
        self.main_page.click_clients_list()
        self.clients_page.is_opened()
        self.clients_page.search_field("тест")
        self.clients_page.search_click()
        self.clients_page.make_screenshot("Успех")