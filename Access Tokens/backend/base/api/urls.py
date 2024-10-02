from django.urls import path
from . import views
from .views import MyTokenObtainPairView, signup, user_skills

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)


urlpatterns = [
    path('', views.getRoutes),
    path('token/refresh/', TokenRefreshView.as_view(), name='refresh_token'),
    path('signup/', signup, name='signup'),
    path('token/', MyTokenObtainPairView.as_view(), name='get_token'),
    path('skills/', user_skills, name='user-skills'),
]
