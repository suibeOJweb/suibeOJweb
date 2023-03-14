from django.shortcuts import render, HttpResponse

# Create your views here.


def index(request):
    return render(request, "index.html")

def login(request):

    if request.method == 'POST':
        userAccount = request.POST.get('userAccount')
        password = request.POST.get('password')
        return render(request,'log_in.html', locals())
    return render(request, "log_in.html")

def register(request):
    return render(request, "register.html")


