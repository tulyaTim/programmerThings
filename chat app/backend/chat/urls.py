from django.urls import path
from . import views

urlpatterns = [
    path('messages/<int:user_id>/', views.private_messages, name='private_messages'),
]
