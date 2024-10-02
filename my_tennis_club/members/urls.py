from django.urls import path
from . import views

app_name = "cyclone"

urlpatterns = [
    path('', views.main, name="main"),
    path('members/', views.all_members, name="members"),
    path('' ,views.members, name="testing"),
    path('signup/', views.signupView, name="signup"),
    path('accounts/login/', views.loginView, name="login"),
    path('members/details/<slug:slug>', views.details, name="details"),
    path('logout/', views.logoutView, name='logout'),
]
