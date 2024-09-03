from . import views
from django.urls import path

app_name = 'dashboard'

urlpatterns = [
    path('', views.community_view, name='community'),
    path('profile/', views.create_profile, name='create_profile'),
    path('post/', views.add_post, name='add_post'),
    path('like/', views.like_post, name='like_post'),
    path('accounts/login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
]
