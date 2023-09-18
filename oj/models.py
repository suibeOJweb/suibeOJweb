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
    password = models.CharField(max_length=32, verbose_name="用户密码")
    scores = models.IntegerField(verbose_name="积分", default=0)
    introduction = models.TextField(verbose_name="简介", default="该用户很懒……什么也没留下")
    userRole = models.SmallIntegerField(verbose_name="用户角色", default=1, choices=roles)
    nickName = models.CharField(max_length=32, verbose_name="用户昵称")
    email = models.EmailField(verbose_name="用户邮箱", null=True)
    correctNum = models.PositiveIntegerField(verbose_name="刷题量", default=0)
    enrollmentYear = models.CharField(max_length=8, verbose_name="入学年份",null=True)
    createTime = models.DateTimeField(verbose_name="注册时间", null=True)
    updateTime = models.DateTimeField(verbose_name="信息更新时间",null=True)
    deleted = models.BooleanField(verbose_name="用户是否注销", default=0)
    avatarUrl = models.CharField(max_length=64, verbose_name="头像url" , default= "/media/defaul.jpg")

class Score(models.Model):
    scoreId = models.BigAutoField(primary_key=True)
    scoreChangeNum = models.IntegerField(verbose_name="积分更改数")
    reason = models.TextField(verbose_name="积分更改原因")
    suiberId = models.ForeignKey("Suiber", to_field="suiberId", on_delete=models.CASCADE, db_column="suiberId")
    createTime = models.DateTimeField(verbose_name="积分更改时间")

class Question(models.Model):
    questionId = models.AutoField(primary_key = True)
    questionTitle = models.TextField(verbose_name= "问题标题")
    questionContent = models.TextField(verbose_name= "问题内容")
    difficulty = models.CharField(max_length=8, verbose_name= "难度")
    limits = models.CharField(max_length=12, verbose_name= "限制")
    totalPass = models.IntegerField(verbose_name="总通过数", default=0)
    totalTry = models.IntegerField(verbose_name="总尝试数", default=0)
    createTime = models.DateTimeField(verbose_name="问题创建时间")


