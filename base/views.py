from django.shortcuts import render
from .models import Contact, Subscriber
from .utils import subscribers

# Create your views here.

def home(request):
    subscribers(request)
    return render(request, 'base/home.html')

def about(request):
    subscribers(request)
    return render(request, 'base/about.html')

def testimonials(request):
    subscribers(request)
    return render(request, 'base/testimonials.html')

def services(request):
    subscribers(request)
    return render(request, 'base/services.html')

def portfolio(request):
    subscribers(request)
    return render(request, 'base/portfolio.html')

def contact(request):
    if request.method == 'POST':
        if 'contact' in request.POST:
            name = request.POST['name']
            email = request.POST['email']
            phone = request.POST['phone']
            message = request.POST['message']
            contact = Contact(name = name, email = email, phone = phone, message = message)
            contact.save()
    subscribers(request)
    return render(request, 'base/contact.html')


    