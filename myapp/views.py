from django.shortcuts import render, HttpResponse, redirect
from myapp.models import UserInfo, Department
from myapp.utils.pagination import Pagination


def index(request):
    # request.method : GET/POST
    # request.GET : 获取url参数
    # request.POST: 获取body参数
    print(request, 'request ------------')
    info = request.session.get('info')
    if not info:
        return redirect("/login")

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
        # 生成随机字符串，写入到客户端cookie中，再写入到session中
        request.session['info'] = "123"
        return redirect('/index')
    # return HttpResponse('登陆失败')
    return render(request, 'login.html', {'error_msg': '登陆失败，用户名或密码错误'})


def create_user(request):
    UserInfo.objects.create(username="test", password="123", age=12)
    Department.objects.create(name="department one")
    # for i in range(20):
    #     UserInfo.objects.create(username="test"+str(i), password="123", age=1, depart_id=1, gender=1)

    return HttpResponse("添加成功")


def delete_user(request):
    UserInfo.objects.filter(id=3).delete()
    return HttpResponse("删除成功")


def query_user(request):
    # QuerySet类型
    data_list = UserInfo.objects.all()
    for data in data_list:
        pass
        # print(data.username, data.password)
    user_one = UserInfo.objects.filter(id=1).first()
    print(user_one.username)

    # 通过字典方式进行查询
    filter_dict = {}
    value = request.GET.get('username')
    if value:
        filter_dict["username"] = value
    # 分页
    page = request.GET.get('page') or 1
    page_size = request.GET.get('page_size') or 10
    start = (page - 1) * page_size
    end = page * page_size

    page_object = Pagination(request)

    dict_filter_data = UserInfo.objects.filter(**filter_dict).order_by("id")[page_object.start:page_object.end]
    dict_filter_count = UserInfo.objects.filter(**filter_dict).count()
    print(dict_filter_data)
    print(dict_filter_count, '========dict_filter_count')

    # 数字
    # id = 12 等于，id__gt = 12 大于，id__gte = 12 大于等于；id__lt = 12 小于，id__lte 小于等于
    id_filter_data = UserInfo.objects.filter(id__gt=0)
    print(id_filter_data)

    # 字符串
    # __startswith __endswith __contains
    username_filter_data = UserInfo.objects.filter(username__contains="t")
    print(username_filter_data)

    return HttpResponse("查询成功")


def update_user(request):
    UserInfo.objects.filter(id=1).update(password="new_password")
    return HttpResponse("update success")
