from django.shortcuts import render, HttpResponse


def index(request):
    print(request, 'request ------------')
    return HttpResponse("欢迎使用")


def user_list(request):
    print(request, 'user list request -------')
    return HttpResponse("用户列表")


def user_add(request):
    print(request, 'user add request -------')
    # 优先去根目录下templates中寻找，要在settings中配置
    # 根据app注册顺序寻找
    # 去当前app下寻找templates寻找user_add.html
    return render(request, 'user_add.html')
