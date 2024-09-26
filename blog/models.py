from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


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
    title = models.CharField(max_length=200) #Título do post
    content = RichTextField()  # Campo com CKEditor
    autor = models.ForeignKey(User,on_delete=models.CASCADE) #Autor do post(Usuário do Django)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)  #Categoria do post
    tags = models.CharField(max_length=100,blank=True) #Tags do post
    create_at = models.DateTimeField(auto_now_add=True) #Data de criação
    updated_at = models.DateTimeField(auto_now=True)  #Data de atualização
    image = models.ImageField(upload_to='post_images/', null=True, blank=True)  # Aqui, a imagem será opcional (null=True, blank=True), e o diretório onde as imagens serão salvas será post_images/.

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