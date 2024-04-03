from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def blog_view(request):
    return render (request, 'blog/blog-home.html')
def blog_single(request):
    context = {'title': 'bitcoin crashed again!', 'content':'bitcoin was flying but now grounded as always', 'author': 'Behzad Abbasi'}
    return render (request, 'blog/blog-single.html', context)