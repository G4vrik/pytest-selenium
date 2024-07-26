import allure
import pytest
from base.base_test import BaseTest


@allure.feature("Проверка авторизации")
class TestLogin(BaseTest):

    @allure.title("Проверка авторизации")
    @allure.severity("critical")
    @pytest.mark.smoke
    def test_search(self):
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_submit_button()
        self.main_page.is_opened_main()
        