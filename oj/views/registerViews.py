from django.shortcuts import render
# Create your views here.
from oj import models
import random

def get_nickName():
    usableName_char = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+=-><:}{?/"  # 可作为用户名的字符
    e_userName = []  # 定义一个临时List变量,使用list.append添加字符
    for i in range(8):
        e_userName.append(random.choice(usableName_char))
    userName = ''.join(e_userName)
    return userName


def register(request):
    successMessage = '注册成功'
    registerErrMessage = '注册失败'
    userExistMessage = '用户名已经存在'
    if request.method == 'POST':
        userAccount = request.POST.get('userAccount')
        password = request.POST.get('password')
        checkPassword = request.POST.get('checkPassword')

        userinfo = models.Suiber.objects.filter(account = userAccount)
        if userinfo.exists():
            return render(request , 'register.html' , {'errMessage': userExistMessage})
        # 校验密码.
        if password == checkPassword :
            randomNickName = '默认用户' + get_nickName()
            models.Suiber.objects.create(
                account=userAccount,
                password=password,
                nickName= randomNickName

            )
        else:
            return render(request, 'register.html', {'errMessage': registerErrMessage})
        return render(request, 'log_in.html', {'successMessage': successMessage})
    return render(request, "register.html")