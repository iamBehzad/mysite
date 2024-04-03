import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

from django.urls import path
from blog.views import *
app_name= 'blog'
urlpatterns = [
    path('',blog_view, name='index'),
    path('single',blog_single, name='single')
]
