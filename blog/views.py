from django.shortcuts import render,get_object_or_404
from blog.models import Post
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

from django.http import HttpResponse

def blog_view(request, cat_name=None, author_username=None):
    current_time = timezone.now()
    posts = Post.objects.filter(status =1 ,published_date__lte=current_time)
    if cat_name:
        posts = posts.filter(category__name = cat_name)
    if author_username:
        posts = posts.filter(author__username = author_username)    
        
    posts = Paginator(posts,3)
    try:
        page_number=request.GET.get('page')
        posts = posts.page(page_number)
    except EmptyPage: 
        posts= posts.get_page(1)
    except PageNotAnInteger:
        posts = posts.get_page(1)


    context = {'posts': posts}
    return render (request, 'blog/blog-home.html',context)

def blog_single(request, pid):
    current_time = timezone.now()
    
    post = get_object_or_404(Post,pk=pid, status =1 ,published_date__lte=current_time)
    
    post.counted_view += 1
    post.save()
    
    next_post = Post.objects.filter(status =1 ,published_date__lte=current_time, id__gt=pid).order_by('pk').first()
    
    previous_post = Post.objects.filter(status =1 ,published_date__lte=current_time, id__lt=pid).order_by('pk').last()
        
    context = {
        'post': post,  
        'next_post': next_post,
        'previous_post': previous_post
        }
    
    return render (request, 'blog/blog-single.html', context)

def blog_category(request, cat_name):
    current_time = timezone.now()
    posts = Post.objects.filter(status =1 ,published_date__lte=current_time)
    posts = posts.filter(category__name = cat_name)
    context= {'posts': posts}
    return render(request, 'blog/blog-home.html', context)

def blog_search(request):
    current_time = timezone.now()
    posts = Post.objects.filter(status =1 ,published_date__lte=current_time)
    if request.method == 'GET':
        if s:=request.GET.get('s'):
            posts=posts.filter(content__contains=s)
    context = {'posts': posts}
    return render (request, 'blog/blog-home.html',context)