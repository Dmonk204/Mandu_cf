from django.contrib import admin
from base.models import Contact, Subscriber
from django.contrib.auth.models import Group

# Register your models here.

admin.site.site_header = "Mandu Clearing and Forwarding Agency"
admin.site.site_title = "Mandu Clearing and Forwarding"
admin.site.index_title = "Welcome to Mandu Clearing and Forwarding Agency"

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email')
    
admin.site.register(Contact,ContactAdmin)
admin.site.register(Subscriber)
admin.site.unregister(Group)
