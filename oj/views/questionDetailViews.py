from django.shortcuts import render
# Create your views here.
from oj import models

def questionDetail(request,id):
    data = models.Question.objects.get(questionId=id)
    return render(request,'questionDetail.html',locals())