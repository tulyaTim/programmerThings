from django.urls import path
from. import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.index, name='index'),
    path('members/', views.all_members, name='all_members'),
    path('signup/', views.signup_view, name='signup'),
    path('accounts/login/', views.login_view, name='login'),
    path('add_members/', views.add_members, name='add_members'),
    path('logout/', views.logout_view, name='logout'),
]
