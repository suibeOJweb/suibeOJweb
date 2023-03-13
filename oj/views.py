from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

#
# def log(request):
#     u = request.GET.get("user")
#     p = request.GET.get("pwd")
#     if p and u:
#         return redirect("/oj/")
#     else:
#         return HttpResponse("用户名或密码错误")


def index(request):
    return render(request, "index.html")


def login(request):
    return render(request, "log_in.html")


def register(request):
    return HttpResponse('注册页面！')


