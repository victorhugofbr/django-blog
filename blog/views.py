from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from .models import Post
from django import forms

"""
Criação de duas views principais:
Listar posts: Uma página que mostra todos os posts do blog.
Detalhar posts: Um página individual que mostra o conteúdo de um post e seus comentários.
"""

#View para listar os posts
def post_list(request):
    posts = Post.objects.all().order_by('-create_at')  # Usando 'create_at' corretamente
    return render(request, 'blog/post_list.html', {'posts': posts})

#View para detalhar um post.
def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'blog/post_detail.html', {'post': post})


# Formulário para o Post
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'category', 'tags','image']

# View para criar um novo post
@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)  #request.FILES para lidar com uploads de arquivos
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user  # Associa o post ao usuário logado
            post.save()
            return redirect('post_list')  # Redireciona para a página de listagem de posts
        else:
            # Se o formulário for inválido, renderiza a página com erros
            return render(request, 'blog/post_create.html', {'form': form})

    else:
        form = PostForm()  # Cria um formulário vazio no método GET
    return render(request, 'blog/post_create.html', {'form': form})  # Retorna a página com o formulário