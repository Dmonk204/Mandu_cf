from django.shortcuts import render
from .models import Contact

# Create your views here.

def home(request):
    return render(request, 'base/home.html')

def about(request):
    return render(request, 'base/about.html')

def testimonials(request):
    return render(request, 'base/testimonials.html')

def services(request):
    return render(request, 'base/services.html')

def portfolio(request):
    return render(request, 'base/portfolio.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        contact = Contact(name = name, email = email, phone = phone, message = message)
        contact.save()
    else:
        print('hellooooooooo')
    return render(request, 'base/contact.html')