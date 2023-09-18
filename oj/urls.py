from django.urls import path, re_path
from .views import IndexViews,loginViews, registerViews,userCenterViews,questionDetailViews

urlpatterns = [
    path("", IndexViews.index, name="index"),
    path('login/', loginViews.login, name='login'),
    path('register/', registerViews.register, name='register'),
    re_path(r'userCenter/(?P<id>\d{1,2})',userCenterViews.userCenter, name = 'userCenter'),
    path('logout/',IndexViews.user_logout,name = 'logout'),
    re_path(r'questionDetail/(?P<id>\d{1,2})', questionDetailViews.questionDetail, name = 'questionDetail')
]

