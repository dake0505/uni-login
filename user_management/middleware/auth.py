from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect


class Middleware(MiddlewareMixin):
    def process_request(self, request):
        if request.path_info == 'login':
            return
        info = request.session.get('info')
        if info:
            return
        return redirect('login')

    def process_response(self, request, response):
        return response
