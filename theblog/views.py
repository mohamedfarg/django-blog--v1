from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Category
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.core.paginator import Paginator

from .forms import *

def post_list(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 5) # Show 5 objects per page

    page = request.GET.get('page')
    objects = paginator.get_page(page)

    return render(request, 'posts/index.html', { 'posts': objects })

def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    comments = Comment.objects.all().order_by('-published_date')[0:3]
    form = CommentForm()
    return render(request, 'posts/post.html', {
        'comments': comments,
        'post':post,
        'form': form,
    })
   

def post_manage(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 5) # Show 5 objects per page

    page = request.GET.get('page')
    objects = paginator.get_page(page)

    return render(request, 'posts/manage_posts.html', { 'posts': objects })
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'blog/category_list.html', {'categories': categories})

def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    posts = Post.objects.filter(categories=category)
    return render(request, 'blog/category_detail.html', {'category': category, 'posts': posts})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            form.save_m2m()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'posts/addpost.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            form.save_m2m()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')


#comments

def comments(request,id):
    
    post = get_object_or_404(Post, id=id)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment = Comment(
            post = post,
            author = request.user,
                content=form.cleaned_data['content'],
            )
            comment.save()

    return redirect('post_detail',id=post.id)