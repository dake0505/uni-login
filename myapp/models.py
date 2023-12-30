from django.db import models


# Create your models here.
class UserInfo(models.Model):
    objects = models.Manager()
    username = models.CharField(verbose_name="用户名", max_length=32)
    password = models.CharField(max_length=64)
    age = models.IntegerField()
    create_time = models.DateTimeField(verbose_name="创建时间", null=True, blank=True)
    update_time = models.DateTimeField(verbose_name="更新时间", null=True, blank=True)
    desc = models.CharField(null=True, blank=True, max_length=64)
    # 无约束
    # depart_id = models.BigIntegerField(verbose_name="部门ID")

    # 有约束 to: 与表关联， to_field: 与列关联。
    # 并且会自动生成depart_id列
    # 1. 级联删除，models.CASCADE，depart表中被删除后，user也会被删除
    # 2. 可以置空，models.SET_NULL，注意 null=True blank=True
    depart = models.ForeignKey(to="Department", to_field="id", on_delete=models.CASCADE)
    # django中的约束
    gender_choices = (
        (1, 'male'),
        (2, 'female')
    )
    gender = models.SmallIntegerField(verbose_name="性别", choices=gender_choices)


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
