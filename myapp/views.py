from django.shortcuts import render, HttpResponse, redirect
from myapp.models import UserInfo, Department


def index(request):
    # request.method : GET/POST
    # request.GET : 获取url参数
    # request.POST: 获取body参数
    print(request, 'request ------------')

    # 返回字符串
    return HttpResponse("欢迎使用")


def baidu(request):
    # 重定向
    return redirect("https://www.baidu.com")


def user_list(request):
    print(request, 'user list request -------')
    import requests
    res = requests.get('https://www.baidu.com')
    print(res, '------')
    return HttpResponse(res)


def user_add(request):
    print(request, 'user add request -------')
    # 优先去根目录下templates中寻找，要在settings中配置
    # 根据app注册顺序寻找
    # 去当前app下寻找templates寻找user_add.html
    return render(request, 'user_add.html')


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')

    print(request.POST)
    username = request.POST.get('username')
    password = request.POST.get('password')
    if username == 'root':
        # return HttpResponse('登陆成功')
        return redirect('/index')
    # return HttpResponse('登陆失败')
    return render(request, 'login.html', {'error_msg': '登陆失败，用户名或密码错误'})


def create_user(request):
    UserInfo.objects.create(username="test", password="123", age=12)
    Department.objects.create(name="department one")

    return HttpResponse("添加成功")


def delete_user(request):
    UserInfo.objects.filter(id=3).delete()
    return HttpResponse("删除成功")


def query_user(request):
    # QuerySet类型
    data_list = UserInfo.objects.all()
    for data in data_list:
        print(data.username, data.password)
    user_one = UserInfo.objects.filter(id=1).first()
    print(user_one.username)
    # print(data_list)
    return  HttpResponse("查询成功")


def update_user(request):
    UserInfo.objects.filter(id=1).update(password="new_password")
    return HttpResponse("update success")

