from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("chat/<int:user_id>/", views.chat_view, name="chat_view"),
    path("accounts/login/", views.login_view, name='login'),
    path("accounts/signup/", views.signup_view, name='signup')
]
