from django.shortcuts import render
# Create your views here.
from oj import models
def login(request):

    errMessage = '登录失败'
    successfulMessage = '登录成功'
    if request.method == 'POST':
        userAccount = request.POST.get('userAccount')
        password = request.POST.get('password')
        try:
            userinfo = models.Suiber.objects.get(account= userAccount)
        except:
            return render(request, 'log_in.html', {'errMessage': errMessage})

        if password == userinfo.password:
            data = models.Question.objects.all()
            return render(request ,'index.html' , {
                'userRole': userinfo.roles,
                'nickName': userinfo.nickName,
                'avatarUrl': userinfo.avatarUrl,
                'successfulMessage' : successfulMessage,
                'suiberId': userinfo.suiberId,
                'data' : data
            })
        else:
            return render(request, 'log_in.html', {'errMessage': errMessage})

    return render(request, "log_in.html")
