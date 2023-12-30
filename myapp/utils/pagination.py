"""
    自定义分页组件
"""


class Pagination(object):
    def __init__(self, request, page_param="page", page_size=10):
        page = request.GET.get(page_param, 1)
        # 检查字符串是否只包含十进制字符。这种方法只存在于unicode对象。
        if page.isdecimal():
            page = int(page)
        else:
            page = 1

        print(page, type(page))
        self.page = page
        self.page_size = page_size
        self.start = (page - 1) * page_size
        self.end = page * page_size

