from django.urls import path, re_path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    re_path(r'userCenter/(?P<id>\d{1,2})',views.userCenter)
]

