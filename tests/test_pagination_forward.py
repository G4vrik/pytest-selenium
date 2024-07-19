# from pages.clients_page import ClientsPage
# from authorization import authorization

# def test_pagination_forward(browser):
#     authorization(browser)
#     clients_page = ClientsPage(browser)

#     clients_page.open()

#     table_row = clients_page.get_table_row()
#     assert table_row, "Table row is empty"

#     pagination = clients_page.get_pagination()
#     assert pagination, "Pagination is empty"

#     total_pages = clients_page.get_total_pages()
#     # assert total_pages == 28, f"Expected 29 pages, but got {total_pages}"

#     clients_page.click_forward()