from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),  # URL para listar posts
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),  # URL para ver o detalhe do post
]
