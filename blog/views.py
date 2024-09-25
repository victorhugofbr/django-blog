from django.shortcuts import render, get_object_or_404
from .models import Post

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

