# Generated by Django 4.1.7 on 2023-03-07 06:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Suiber",
            fields=[
                ("suiberId", models.AutoField(primary_key=True, serialize=False)),
                ("account", models.CharField(max_length=32, verbose_name="用户账户名")),
                ("password", models.UUIDField(verbose_name="用户密码")),
                ("scores", models.IntegerField(default=0, verbose_name="积分")),
                (
                    "introduction",
                    models.TextField(default="该用户很懒……什么也没留下", verbose_name="简介"),
                ),
                (
                    "userRole",
                    models.SmallIntegerField(
                        choices=[(0, "封号"), (1, "普通用户"), (2, "管理员用户")],
                        default=1,
                        verbose_name="用户角色",
                    ),
                ),
                ("nickName", models.CharField(max_length=32, verbose_name="用户昵称")),
                (
                    "email",
                    models.EmailField(max_length=254, null=True, verbose_name="用户邮箱"),
                ),
                (
                    "correctNum",
                    models.PositiveIntegerField(default=0, verbose_name="刷题量"),
                ),
                ("enrollmentYear", models.CharField(max_length=8, verbose_name="入学年份")),
                ("createTime", models.DateTimeField(verbose_name="注册时间")),
                ("updateTime", models.DateTimeField(verbose_name="信息更新时间")),
                ("deleted", models.BooleanField(default=0, verbose_name="用户是否注销")),
            ],
        ),
        migrations.CreateModel(
            name="Score",
            fields=[
                ("scoreId", models.BigAutoField(primary_key=True, serialize=False)),
                ("scoreChangeNum", models.IntegerField(verbose_name="积分更改数")),
                ("reason", models.TextField(verbose_name="积分更改原因")),
                ("createTime", models.DateTimeField(verbose_name="积分更改时间")),
                (
                    "suiberId",
                    models.ForeignKey(
                        db_column="suiberId",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="oj.suiber",
                    ),
                ),
            ],
        ),
    ]
