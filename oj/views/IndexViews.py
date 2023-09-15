from django.shortcuts import render
# Create your views here.
from oj import models
from django.contrib.auth import logout



def index(request):
    data = models.Question.objects.all()
    return render(request, "index.html", locals())


def user_logout(request):
    logout(request)
    return render(request, "index.html")