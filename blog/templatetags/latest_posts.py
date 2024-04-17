from django import template
from blog.models import Post

register = template.Library()

@register.inclusion_tag('blog/latest_posts.html')
def show_latest_posts(count=6):
    latest_posts = Post.objects.filter(status =1).order_by('-published_date')[:count]
    return {'latest_posts': latest_posts}