from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment

def post_list(request):
    posts = Post.objects.all().order_by('-date_posted')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all().order_by('-date_posted')  # Busca os comentários
    
    if request.method == 'POST':  # Quando o formulário for enviado
        content = request.POST.get('content')
        Comment.objects.create(post=post, author=request.user, content=content)
        return redirect('post-detail', pk=post.id)
    
    return render(request, 'blog/post_detail.html', {'post': post, 'comments': comments})

def post_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        post = Post.objects.create(title=title, content=content)
        return redirect('post-detail', pk=post.id)
    return render(request, 'blog/post_form.html')