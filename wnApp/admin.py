from django.contrib import admin
from .models import Category, Profile, ServiceRide, RideRequest, ContactSubmission, RentalProperty, Application

admin.site.register(Category)
admin.site.register(Profile)
admin.site.register(ServiceRide)
admin.site.register(RideRequest)
admin.site.register(ContactSubmission)
admin.site.register(RentalProperty)
admin.site.register(Application)