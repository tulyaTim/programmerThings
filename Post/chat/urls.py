from django.urls import path
from . import views

app_name = 'chat'

urlpatterns = [
    path('', views.index, name='index'),
    path("<int:user_id>/", views.chat_view, name="chat_view"),
]
