from .models import Subscriber
from django.contrib import messages

def subscribers(request):
    if request.method == 'POST':
        if 'subscribe' in request.POST:
            email = request.POST['email-sub']
            if Subscriber.objects.filter(email = email).exists():
                messages.error(request, 'Sorry, this email is already in our subscription list.')
            else:
                
                subscriber = Subscriber(email = email)
                subscriber.save()
                messages.success(request, 'Email added successfully added to subscription list.')
