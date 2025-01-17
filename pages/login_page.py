import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(BasePage):

    PAGE_URL = Links.LOGIN_PAGE

    USERNAME_FIELD = ("xpath", "//input[@id='basic_login']")
    PASSWORD_FIELD = ("xpath", "//input[@id='basic_password']")
    SUBMIT_BUTTON = ("xpath", "//button[@type='submit']")

    @allure.step("Ввели логин")
    def enter_login(self, login):
        self.wait.until(EC.element_to_be_clickable(self.USERNAME_FIELD)).send_keys(login)

    @allure.step("Ввели пароль")
    def enter_password(self, password):
        self.wait.until(EC.element_to_be_clickable(self.PASSWORD_FIELD)).send_keys(password)

    @allure.step("Нажали кнопку")
    def click_submit_button(self):
        self.wait.until(EC.element_to_be_clickable(self.SUBMIT_BUTTON)).click()