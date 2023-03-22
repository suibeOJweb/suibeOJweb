from django.shortcuts import render, HttpResponse
# Create your views here.
from oj import models


def index(request):
    return render(request, "index.html")


def login(request):

    if request.method == 'POST':
        userAccount = request.POST.get('userAccount')
        password = request.POST.get('password')
        return render(request, 'log_in.html', locals())
    return render(request, "log_in.html")


def register(request):
    successMessage = '注册成功'
    errMessage = '注册失败'
    if request.method == 'POST':
        userAccount = request.POST.get('userAccount')
        password = request.POST.get('password')
        checkPassword = request.POST.get('checkPassword')

        # 校验密码
        if password == checkPassword:
            #TODO:md5加密
            #TODO:默认用户昵称做一下唯一标识（比如用户89231）
            models.Suiber.objects.create(
                account=userAccount,
                password=password,
                nickName='默认用户昵称'
            )
        else:
            return render(request, 'register.html', {'errMessage': errMessage})
        return render(request, 'log_in.html', {'successMessage': successMessage})
    return render(request, "register.html")
