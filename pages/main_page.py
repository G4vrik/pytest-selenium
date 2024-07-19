import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class MainPage(BasePage):

    PAGE_URL = Links.MAIN_PAGE

    MAIN_TITLE = ("xpath", "//div[text()='Главная']")
    CLIENTS = ("xpath", "//span[text()='Клиенты']")
    CLIENTS_LIST = ("xpath", "//span[text()='Список клиентов']")

    # Проверка элемента текста "Главная"
    @allure.step("Нашли элемент 'Главная'")
    def is_opened_main(self): 
        self.wait.until(EC.presence_of_element_located(self.MAIN_TITLE))

    @allure.step("Click on 'Клиенты'")
    def click_clients(self):
        self.wait.until(EC.element_to_be_clickable(self.CLIENTS)).click()

    @allure.step("Click on 'Список клиентов'")
    def click_clients_list(self):
        self.wait.until(EC.element_to_be_clickable(self.CLIENTS_LIST)).click()