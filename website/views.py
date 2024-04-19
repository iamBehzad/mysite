from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from website.models import Contact
from website .forms import ContactForm, NewsletterForm
from django.contrib import messages
def index_view(request):
    return render (request, 'website/index.html')

def about_view(request):
    return render (request, 'website/about.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'your ticket submitted successfully')
        else:
            messages.add_message(request, messages.ERROR, 'your ticket didnt submit')
            
    form=ContactForm()
    return render (request, 'website/contact.html', {'form': form})

def newsletter_view(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'your Email submitted successfully')
            return HttpResponseRedirect('/')

    else:   
         messages.add_message(request, messages.ERROR, 'your Email didnt submit')
         return HttpResponseRedirect('/')

def test_view(request):
    return render (request, 'website/test.html')