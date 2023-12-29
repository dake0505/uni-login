from django.db import models


# Create your models here.
class UserInfo(models.Model):
    objects = models.Manager()
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    age = models.IntegerField()
    desc = models.CharField(null=True, blank=True, max_length=64)


class Department(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=16)


"""
    创建class后，ORM会自动创建表，表名为 myapp_userinfo
    id bigint auto_increment primary key,
    username varchar(32),
    password varchar(32),
    age int,
"""

# UserInfo.objects.create(username="test", password="123", age=12)
