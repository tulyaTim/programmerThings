from django.urls import path
from . import views

app_name = "dashboard"

urlpatterns = [
    path('', views.index, name="index"),
    path('login/', views.login_view, name="login"),
    path('signup/', views.signup_view, name="signup"),
    path('logout/', views.logout_view, name="logout"),
    path('home/', views.home, name='home'),
    path('home/add/', views.add_contact, name="add_contact"),
    path('home/<int:id>/', views.contact_details, name="contact_details"),
]
