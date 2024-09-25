from django.contrib import admin
from .models import Post, Category, Comment

"""
Registrar os models no admin: Para que você possa visualizar e gerenciar esses modelos no painel administrativo do Django, você precisa registrá-los no admin.py do seu app. Adicione o seguinte código:
"""
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Comment)