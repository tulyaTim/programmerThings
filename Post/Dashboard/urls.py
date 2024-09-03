from . import views
from django.urls import path, include

app_name = 'dashboard'

urlpatterns = [
    path('', views.community, name='index'),
    path('add/', views.add_post, name='add_post'),
]
