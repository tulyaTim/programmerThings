from . import views
from django.urls import path, include

app_name = 'dashboard'

urlpatterns = [
    path('', views.community, name='index'),
    path('add/', views.add_post, name='add_post'),
    path('login/', views.login_view, name='login'),
    path('accounts/login/', views.login_required_view, name='login_required'),
    path('signup/', views.signup_view, name='signup'),
    path('logout', views.logout_view, name='logout'),
    path('create/', views.create_user_profile, name="create"),
    path('details/<int:id>', views.details, name='details'),
    path('details/<int:pk>/edit', views.Profile_edit, name='edit'),
]
