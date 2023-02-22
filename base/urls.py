from django.urls import path
from base import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('about/', views.about, name = 'about'),
    path('testimonials/', views.testimonials, name = 'testimonials'),
    path('services/', views.services, name = 'services'),
    path('portfolio/', views.portfolio, name = 'portfolio'),
    path('contact/', views.contact, name = 'contact'),
    
]