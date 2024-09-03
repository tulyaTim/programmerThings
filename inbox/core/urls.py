from . import views
from django.urls import path

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('inbox/', views.inbox, name='inbox'),
    path('conversation/<int:pk>/', views.conversation_detail, name='conversation_detail'),
    path('accounts/login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
]
