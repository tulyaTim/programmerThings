from . import views
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

app_name = "posts"

urlpatterns = [
    path('create/', views.create_post, name="create_post"),
    path('', views.view_posts, name="view_posts"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
