from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse, redirect


class M1(MiddlewareMixin):
    def process_request(self, request):
        # 如果方法中没有返回值（或返回None），则继续向后走
        # 如果有返回值 HttpResponse
        print("M1 connect")

        if request.path_info == '/login':
            return

        info = request.session.get('info')
        if info:
            return
        # return HttpResponse('no auth')
        return redirect('/login')

    def process_response(self, request, response):
        print("M1 response")
        return response


class M2(MiddlewareMixin):
    def process_request(self, request):
        print("M2 connect")

    def process_response(self, request, response):
        print("M2 disconnect")
        return response