import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

from django.urls import path
from website.views import *
app_name= 'website'
urlpatterns = [
    
    path('', coming_soon_view, name='coming_soon'),
    path('<path:path>', coming_soon_view, name='coming_soon'),
    
    path('',index_view, name='index'),
    path('about',about_view, name='about'),
    path('contact',contact_view, name='contact'),
    path('newsletter',newsletter_view, name='newsletter'),    
    path('test',test_view, name='test')    
]
