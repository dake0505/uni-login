from django.db import models


# Create your models here.
class UserInfo(models.Model):
    objects = models.Manager()

    username = models.CharField(verbose_name="用户名", max_length=32)
    password = models.CharField(verbose_name="密码", max_length=64)
    nickname = models.CharField(verbose_name="昵称", max_length=32, blank=True)
    email = models.EmailField(verbose_name="邮箱", blank=True)
    created_at = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="更新时间", auto_now=True)

