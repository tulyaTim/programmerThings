from django.urls import path
from .views import home_view, room_view

urlpatterns = [
    path('', home_view, name='login'),
    path('<str:room_name>/<str:username>/', room_view, name='room'),
]
