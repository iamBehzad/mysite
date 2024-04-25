from django import template
from blog.models import Post,Comments
from blog.models import Category

register = template.Library()

@register.simple_tag
def function(a):
    posts = Post.objects.filter(statuse = 1)
    return posts

@register.filter
def snippet(value):
    return value[0:100]

@register.inclusion_tag('blog/blog-popular-posts.html')
def latestposts(arg=3):
    posts= Post.objects.filter(status =1).order_by('published_date')[:arg]
    return {'posts':posts}

@register.inclusion_tag('blog/blog-post-categories.html')
def postcategories():
    posts= Post.objects.filter(status =1)
    categories = Category.objects.all()
    
    cat_dict = {}
    for name in categories:
        cat_dict[name] = posts.filter(category =name).count()
    return {'categories':cat_dict}

@register.simple_tag(name='comments_count')
def function(pid):
    return Comments.objects.filter(post=pid, approved=True).count()