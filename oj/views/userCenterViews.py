from django.shortcuts import render
# Create your views here.
from oj import models

def userCenter(request,id):
    data = models.Suiber.objects.get(suiberId=id)
    return render(request,'userCenter.html',locals())