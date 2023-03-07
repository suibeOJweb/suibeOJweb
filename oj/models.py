from django.db import models

# Create your models here.


class Suiber(models.Model):
    roles = (
        (0, "封号"),
        (1, "普通用户"),
        (2, "管理员用户")
    )

    suiberId = models.AutoField(primary_key=True)
    account = models.CharField(max_length=32, verbose_name="用户账户名")
    password = models.UUIDField(verbose_name="用户密码")
    scores = models.IntegerField(verbose_name="积分", default=0)
    introduction = models.TextField(verbose_name="简介", default="该用户很懒……什么也没留下")
    userRole = models.SmallIntegerField(verbose_name="用户角色", default=1, choices=roles)
    nickName = models.CharField(max_length=32, verbose_name="用户昵称")
    email = models.EmailField(verbose_name="用户邮箱", null=True)
    correctNum = models.PositiveIntegerField(verbose_name="刷题量", default=0)
    enrollmentYear = models.CharField(max_length=8, verbose_name="入学年份")
    createTime = models.DateTimeField(verbose_name="注册时间")
    updateTime = models.DateTimeField(verbose_name="信息更新时间")
    deleted = models.BooleanField(verbose_name="用户是否注销", default=0)


class Score(models.Model):
    scoreId = models.BigAutoField(primary_key=True)
    scoreChangeNum = models.IntegerField(verbose_name="积分更改数")
    reason = models.TextField(verbose_name="积分更改原因")
    suiberId = models.ForeignKey("Suiber", to_field="suiberId", on_delete=models.CASCADE, db_column="suiberId")
    createTime = models.DateTimeField(verbose_name="积分更改时间")
