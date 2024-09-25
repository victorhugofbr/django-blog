from django.db import models
from django.contrib.auth.models import User

#Modelo de Categoria:
class Category(models.Model):
    name = models.CharField(max_length=50,unique=True) #Unique True para garantir que não teremos duas cateogrias com o mesmo nome


    def __str__(self):
        return self.name

#Modelo de Post:
class Post(models.Model):
    """

    author: Relaciona o post a um autor usando uma chave estrangeira ligada ao modelo User do Django
    category: Relaciona o post a uma categoria, podendo ser nulo ou opcional(daí o null=True e Blank= True)
    created_at e updated_at: Datas automáticas de criação e última atualização.
    """
    title = models.CharField(max_length=20) #Título do post
    content = models.TextField() #Conteúdo do post
    autor = models.ForeignKey(User,on_delete=models.CASCADE) #Autor do post(Usuário do Django)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)  #Categoria do post
    tags = models.CharField(max_length=100,blank=True) #Tags do post
    create_at = models.DateTimeField(auto_now_add=True) #Data de criação
    updated_at = models.DateTimeField(auto_now=True)  #Data de atualização

    def __str__(self):
        return self.title

#Modelo de Comentário
class Comment(models.Model):
    """
    post: Relaciona o comentário ao post correspondente.
    author: O autor do comentário, novamente ligado ao modelo User.
    content: O conteúdo do comentário.
    created_at: Data de criação do comentário.
    """
    post = models.ForeignKey(Post,related_name='comments',on_delete=models.CASCADE) #Relaciona ao post
    author = models.ForeignKey(User,on_delete=models.CASCADE) #Autor do comentário (usuário do Django)
    content = models.TextField() #Conteúdo do comentário
    created_at = models.DateTimeField(auto_now_add=True)  # Data de criação

    def __str__(self):
        return f'Comment by {self.author} on {self.post}'