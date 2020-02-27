from rest_framework.pagination import PageNumberPagination


class CommonPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_num'
    page_query_param = "page"
    max_page_size = 100
