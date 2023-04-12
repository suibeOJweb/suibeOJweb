from django.shortcuts import render, HttpResponse
# Create your views here.
from oj import models


def index(request):
    return render(request, "index.html")


def login(request):
    errMessage = '登录失败'
    successfulMessage = '登录成功'
    if request.method == 'POST':
        userAccount = request.POST.get('userAccount')
        password = request.POST.get('password')

        userinfo = models.Suiber.objects.get(account= userAccount)
        if userinfo :
            if password == userinfo.password:
                return render(request , 'index.html' , {
                    'userRole': userinfo.roles,
                    'nickName': userinfo.nickName,
                    'successfulMessage' : successfulMessage
                })
            else:
                return render(request, 'log_in.html', {'errMessage': errMessage})
        else:
            return render(request , 'log_in.html' , {'errMessage' : errMessage})
    return render(request, "log_in.html")


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
        # 校验密码
        if password == checkPassword :
            models.Suiber.objects.create(
                account=userAccount,
                password=password,
                nickName='用户'
            )
        else:
            return render(request, 'register.html', {'errMessage': registerErrMessage})
        return render(request, 'log_in.html', {'successMessage': successMessage})
    return render(request, "register.html")
