# Generated by Django 4.1.7 on 2023-03-15 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("oj", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="suiber",
            name="createTime",
            field=models.DateTimeField(null=True, verbose_name="注册时间"),
        ),
        migrations.AlterField(
            model_name="suiber",
            name="enrollmentYear",
            field=models.CharField(max_length=8, null=True, verbose_name="入学年份"),
        ),
        migrations.AlterField(
            model_name="suiber",
            name="updateTime",
            field=models.DateTimeField(null=True, verbose_name="信息更新时间"),
        ),
        migrations.AlterField(
            model_name="question",
            name="createTime",
            field=models.DateTimeField(null=True, verbose_name="问题创建时间")
        )
    ]
