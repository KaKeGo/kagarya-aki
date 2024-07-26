from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.utils.urls import replace_query_param


class TaskResultsSetPagination(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_size'
    max_page_size = 1

    def get_paginated_response(self, data):
        current_page = self.page.number
        totla_pages = self.page.paginator.num_pages

        page_range = self.get_page_range(current_page, totla_pages)

        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link(),
                'first': self.get_first_link(),
                'last': self.get_last_link(),
            },
            'current_page': current_page,
            'total_pages': totla_pages,
            'page_range': page_range,
            'results': data,
        })
    
    def get_page_range(self, current_page, totla_pages):
        page_range = []
        if totla_pages <= 7:
            page_range = list(range(1, totla_pages + 1))
        else:
            if current_page <4:
                page_range = list(range(1, 6)) + ['...', totla_pages]
            elif current_page > totla_pages - 4:
                page_range = [1, '...'] + list(range(totla_pages - 4, totla_pages + 1))
            else:
                page_range = [1, '...'] + list(range(current_page - 1, current_page + 2)) + ['...', totla_pages]
        return page_range
    
    def get_first_link(self):
        if not self.page.has_previous():
            return None
        url = self.request.build_absolute_uri()
        return replace_query_param(url, self.page_query_param, 1)
    
    def get_last_link(self):
        if not self.page.has_next():
            return None
        url = self.request.build_absolute_uri()
        return replace_query_param(url, self.page_query_param, self.page.paginator.num_pages)

