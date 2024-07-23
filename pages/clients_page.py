import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class ClientsPage(BasePage):

    PAGE_URL = Links.CLIENTS_PAGE

    SEARCH_FIELD = ("xpath", "//input[@placeholder='Введите имя или ID клиента']")
    SEARCH_BUTTON = ("xpath", "(//button[@type='button'])[3]")

    @allure.step("Заполнили поле поиска")
    def search_field(self, name):
        search_field = self.wait.until(EC.element_to_be_clickable(self.SEARCH_FIELD))
        search_field.click()
        search_field.send_keys(name)

    @allure.step("Нажали на кнопку поиска")
    def search_click(self):
        self.wait.until(EC.element_to_be_clickable(self.SEARCH_BUTTON)).click()