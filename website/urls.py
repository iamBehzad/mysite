import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

from django.urls import path
from website.views import *

urlpatterns = [
    path('',index_view),
    path('about',about_view),
    path('contact',contact_view)
]
