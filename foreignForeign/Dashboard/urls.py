from . import views
from django.urls import path

app_name = 'Dashboard'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('profile/', views.create_profile, name='profile'),
    path('logout/', views.logout_view, name='logout')
]
