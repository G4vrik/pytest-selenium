# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# class ExamplePage:
#     def __init__(self, browser):
#         self.browser = browser
#         self.url = "https://www.example.com"
#         self.header_locator = (By.TAG_NAME, "h1")

#     def open(self):
#         self.browser.get(self.url)

#     def get_header_text(self):
#         header = WebDriverWait(self.browser, 10).until(
#             EC.presence_of_element_located(self.header_locator)
#         )
#         return header.text