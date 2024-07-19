import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_page import BasePage
from config.links import Links


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

    # def __init__(self, browser):
        # self.browser = browser
        # self.url = "https://dev-react.iwater-crm.online/"
        
        # Локаторы
        # self.username_input = (By.ID, "basic_login")
        # self.password_input = (By.ID, "basic_password")
        # self.login_button = (By.XPATH, "//button[@type='submit']") # Нажать на кнопку
        # self.locator = (By.XPATH, "//*[text()='Главная']")

    # Открыть страницу
    # def open(self):
    #     self.browser.get(self.url)
        
    # Ввести логин
    # def enter_username(self, username):
    #     username_field = WebDriverWait(self.browser, 10).until(
    #         EC.presence_of_element_located(self.username_input)
    #     )
    #     username_field.send_keys(username)
    

    # Ввести пароль
    # def enter_password(self, password):
    #     password_field = WebDriverWait(self.browser, 10).until(
    #         EC.presence_of_element_located(self.password_input)
    #     )
    #     password_field.send_keys(password)
    

    # Нажать на кнопку "Войти"
    # def click_login(self):
    #     login_button = WebDriverWait(self.browser, 10).until(
    #         EC.element_to_be_clickable(self.login_button)
    #     )
    #     login_button.click()


    # def get_header_text(self):
    #     header = WebDriverWait(self.browser, 10).until(
    #         EC.presence_of_element_located(self.locator)
    #     )
    #     return header.text