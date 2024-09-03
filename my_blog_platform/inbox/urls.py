from . import views
from django.urls import path

app_name = "inbox"

urlpatterns = [
    path('home/<int:id>/inbox', views.display_message, name="display_message"),
]
