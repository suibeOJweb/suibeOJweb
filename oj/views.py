from django.shortcuts import render, HttpResponse

# Create your views here.


def index(request):
    return render(request, "index.html")

def login(request):
    return render(request, "log_in.html")

def register(request):
    return HttpResponse('注册页面！')


