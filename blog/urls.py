from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),  # Lista de posts
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),  # Detalhe de post
    path('post/new/', views.post_create, name='post_create'),  # Criação de novo post
]