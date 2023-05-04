from django.shortcuts import render, HttpResponse
# Create your views here.
from oj import models


def index(request):
    data = models.Question.objects.all()
    return render(request, "index.html", locals())


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
                    'avatarUrl': userinfo.avatarUrl,
                    'successfulMessage' : successfulMessage,
                    'suiberId': userinfo.suiberId
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
        # 校验密码.
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

def userCenter(request,id):
    data = models.Suiber.objects.get(suiberId=id)
    return render(request,'userCenter.html',locals())