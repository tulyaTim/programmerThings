from django.contrib import admin
from django.urls import re_path, path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('signup/', views.signup),
    re_path('login/', views.login),
    re_path('test_token', views.test_token),
]
