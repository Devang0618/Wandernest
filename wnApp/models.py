from django.contrib.auth.models import User
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Profile(models.Model):
    GENDER_CHOICES = [
        ('','Select Gender #new default option functionality ;)'),
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    COUNTRY_CHOICES = [
        ('','Select Country'),
        ('IND', 'India'),
        ('US', 'United States'),
        ('AUS', 'Australia'),
    ]
    INDSTATE_CHOICES = [
        ('','Select State'),
        ('GUJ', 'Gujarat'),
        ('M', 'Madhya Pradesh'),
        ('AS', 'Assam'),
    ]
    INDCITY_CHOICES = [
        ('','Select City'),
        ('AHM', 'Ahmedabad'),
        ('GN', 'Gandhinagar'),
        ('MEH', 'Mehsana'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    country = models.CharField(max_length=100, blank=True, choices=COUNTRY_CHOICES)
    state = models.CharField(max_length=100, blank=True, choices=INDSTATE_CHOICES)
    city = models.CharField(max_length=100, blank=True, choices=INDCITY_CHOICES)
    mobile_no = models.CharField(max_length=15, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    birth_date = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    email = models.EmailField()
    vehicle_number = models.CharField(max_length=100, blank=True)
    license_number = models.CharField(max_length=100, blank=True)
    #current_location = models.CharField(max_length=255, blank=True)
    address = models.CharField(max_length=255, blank=True)
    room = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.user.username

class ServiceRide(models.Model):
    driver = models.ForeignKey(Profile, related_name='posted_rides', on_delete=models.CASCADE)
    current_location = models.CharField(max_length=255)
    destination_location = models.CharField(max_length=255)
    status = models.CharField(max_length=10, default='Available')  # 'Available', 'Approved', 'Rejected'

class RideRequest(models.Model):
    rider = models.ForeignKey(Profile, related_name='ride_requests', on_delete=models.CASCADE)
    service_ride = models.ForeignKey(ServiceRide, related_name='requests', on_delete=models.CASCADE)
    status = models.CharField(max_length=10, default='Pending')  # 'Pending', 'Approved', 'Rejected'

# models.py
class RentalProperty(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='property_photos')
    num_rooms = models.IntegerField()
    address = models.CharField(max_length=255)
    additional_details = models.TextField()
    is_available = models.BooleanField(default=True)

class Application(models.Model):
    tenant = models.ForeignKey(User, on_delete=models.CASCADE)
    rental_property = models.ForeignKey(RentalProperty, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, default='Pending')

'''#-------------------------------------------------------------------------------
class ServiceOwner(models.Model):
    owner = models.ForeignKey(Profile, related_name='posted_rides', on_delete=models.CASCADE)
    address_o = models.CharField(max_length=255)
    room_o = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    status = models.CharField(max_length=10, default='Available')  # 'Available', 'Approved', 'Rejected'

class StayingRequest(models.Model):
    tenant = models.ForeignKey(Profile, related_name='ride_requests', on_delete=models.CASCADE)
    service_staying = models.ForeignKey(ServiceRide, related_name='requests', on_delete=models.CASCADE)
    status = models.CharField(max_length=10, default='Pending')  # 'Pending', 'Approved', 'Rejected'
    '''
    
class ContactSubmission(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    