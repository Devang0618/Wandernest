# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Application, Profile, RentalProperty, ServiceRide, RideRequest, ContactSubmission        # ServiceOwner, StayingRequest

class RegistrationForm(UserCreationForm):
    name = forms.CharField(max_length=100)
    birth_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    gender = forms.ChoiceField(choices=Profile.GENDER_CHOICES)
    email = forms.EmailField()
    country = forms.ChoiceField(choices=Profile.COUNTRY_CHOICES)  # Add country field
    state = forms.ChoiceField(choices=Profile.INDSTATE_CHOICES)    # Add state field
    city = forms.ChoiceField(choices=Profile.INDCITY_CHOICES)     # Add city field
    mobile_no = forms.CharField(max_length=15) # Add mobile number field

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'name', 'birth_date', 'gender', 'email', 'country', 'state', 'city', 'mobile_no']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['vehicle_number', 'license_number', 'address', 'room']

class ServiceRideForm(forms.ModelForm):
    class Meta:
        model = ServiceRide
        fields = ['current_location', 'destination_location']

class RideRequestForm(forms.ModelForm):
    class Meta:
        model = RideRequest
        fields = []
        
# forms.py
class RentalPropertyForm(forms.ModelForm):
    class Meta:
        model = RentalProperty
        fields = ['photo', 'num_rooms', 'address', 'additional_details']

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = []

        '''#---------------------------------------------------------------
class ServiceOwnerForm(forms.ModelForm):
    class Meta:
        model = ServiceOwner
        fields = ['address_o', 'room_o']

class StayingRequestForm(forms.ModelForm):
    class Meta:
        model = StayingRequest
        fields = []'''

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactSubmission
        fields = ['name', 'email', 'message']
