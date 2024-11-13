from . import views
from django.urls import path

app_name = 'accounts'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),

    path('profile/<int:id>/', views.profile, name='profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
]
