from . import views
from django.urls import path, include

app_name = 'dashboard'

urlpatterns = [
    path('', views.community, name='index'),
    path('add/', views.add_post, name='add_post'),
    path('accounts/login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
]
