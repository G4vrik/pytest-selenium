import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from base.base_page import BasePage
from config.links import Links


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

    # def __init__(self, browser):
    #     self.browser = browser
    #     self.url = "https://dev-react.iwater-crm.online/clients/clientsList"
    #     self.table_row = (By.CSS_SELECTOR, ".ant-table-row.ant-table-row-level-0") # Ищем строку таблицы
    #     self.pagination_items = (By.CSS_SELECTOR, ".ant-pagination.css-m2jir1") # Ищем элементы пагинации
    #     self.pagination_forward = (By.XPATH, '//*[@title="Вперед"]') # Ищем стрелку "Вперед"
    #     self.last_page_item = (By.CSS_SELECTOR, "ul.ant-pagination li.ant-pagination-item") # Ищем последнюю страницу пагинации

    # def open(self):
    #     self.browser.get(self.url)

    # def get_table_row(self):
    #     row = WebDriverWait(self.browser, 10).until(
    #         EC.presence_of_element_located(self.table_row)
    #     )
    #     return row
    
    # def get_pagination(self):
    #     elem_page = WebDriverWait(self.browser, 10).until(
    #         EC.presence_of_element_located(self.pagination_items)
    #     )
    #     return elem_page

    # def get_total_pages(self):
    #     page_items = self.browser.find_elements(*self.last_page_item)
    #     return int(page_items[-1].text)
    
    # # def click_forward(self):
    # #     forward = WebDriverWait(self.browser, 10).until(
    # #         EC.element_to_be_clickable(self.pagination_forward)
    # #     )
    # #     forward.click()

    # def click_forward(self):
    #     total_pages = self.get_total_pages()
    #     current_page = 1 # Можно будет изменить на метод поиска текущей страницы
    #     while current_page < total_pages:
    #         try:
    #             forward = WebDriverWait(self.browser, 10).until(
    #                 EC.element_to_be_clickable(self.pagination_forward)
    #             )
    #             forward.click()
    #             current_page += 1
                
    #             # Ожидание загрузки таблицы
    #             self.get_table_row()
                
    #         except (TimeoutException, NoSuchElementException):
    #             break
        
    #     print(f"Reached the last page or encountered an error. Current page: {current_page}")
    #     return current_page