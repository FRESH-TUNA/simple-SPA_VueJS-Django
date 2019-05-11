from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.readPosts),
    path('<int:pk>', views.readPost),
    path('create', views.createPost),
    path('<int:pk>/update', views.updatePost),
    path('<int:pk>/delete', views.deletePost),
]