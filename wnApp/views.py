from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Application, Category, Profile, RentalProperty, ServiceRide, RideRequest, ContactSubmission      # ServiceOwner, StayingRequest
from .forms import ApplicationForm, RegistrationForm, ProfileForm, RentalPropertyForm, ServiceRideForm, RideRequestForm, ContactForm     # ServiceOwnerForm, StayingRequestForm

def home(request):
    return render(request, 'wnApp/home.html')

def about(request):
    return render(request, 'wnApp/about.html')

def contact(request):
    return render(request, 'wnApp/contact.html')

def riding(request):
    return render(request, 'wnApp/riding.html')

def staying(request):
    return render(request, 'wnApp/staying.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            name = form.cleaned_data.get('name')
            birth_date = form.cleaned_data.get('birth_date')
            gender = form.cleaned_data.get('gender')
            email = form.cleaned_data.get('email')
            mobile_no = form.cleaned_data.get('mobile_no')
            country = form.cleaned_data.get('country')
            state = form.cleaned_data.get('state')
            city = form.cleaned_data.get('city')
            category_id = request.POST.get('category')
            category = Category.objects.get(id=category_id)
            profile = Profile.objects.create(user=user, category=category, name=name, birth_date=birth_date, gender=gender, email=email, mobile_no=mobile_no, country=country, state=state, city=city)
            return redirect('login')
    else:
        form = RegistrationForm()
    categories = Category.objects.all()
    return render(request, 'wnApp/register.html', {'form': form, 'categories': categories})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            # Redirect user to their respective dashboard based on category
            profile = Profile.objects.get(user=user)
            if profile.category.name == 'Driver':
                return redirect('dashboard_driver')
            elif profile.category.name == 'Rider':
                return redirect('dashboard_rider')
            elif profile.category.name == 'Owner':
                return redirect('dashboard_owner')
            elif profile.category.name == 'Tenant':
                return redirect('dashboard_tenant')
    else:
        form = AuthenticationForm()
    return render(request, 'wnApp/login.html', {'form': form})

@login_required
def logout(request):
    auth_logout(request)
    return redirect('home')

@login_required
def dashboard_driver(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    if profile.category.name != 'Driver':
        return render(request, 'wnApp/dashboard_error.html')  # Display error page if user's category is not Driver
    service_rides = ServiceRide.objects.filter(driver=profile)
    ride_requests = RideRequest.objects.filter(service_ride__driver=profile)
    form = ServiceRideForm()  # Create an instance of the ServiceRideForm
    context = {
        'user_data': {
            'username': user.username,
            'name': profile.name,
            'birth_date': profile.birth_date,
            'gender': profile.get_gender_display(),
            'email': profile.email,
            'profile_name': profile.category.name,
        },
        'service_rides': service_rides,
        'ride_requests': ride_requests,
        'form': form,  # Pass the form to the template context
    }
    return render(request, 'wnApp/dashboard_driver.html', context)

@login_required
def dashboard_rider(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    if profile.category.name != 'Rider':
        return render(request, 'wnApp/dashboard_error.html')  # Display error page if user's category is not Rider
    
    if request.method == 'POST':  # Check if the request is a POST request (form submission)
        form = RideRequestForm(request.POST)
        if form.is_valid():
            ride_request = form.save(commit=False)
            ride_request.rider = profile
            ride_request.save()
            messages.success(request, 'Your request has been sent successfully.')  # Display success message
            return redirect('dashboard_rider')  # Redirect to the dashboard after request submission
    else:
        form = RideRequestForm()

    service_rides = ServiceRide.objects.filter(status='Available')
    context = {
        'user_data': {
            'username': user.username,
            'name': profile.name,
            'birth_date': profile.birth_date,
            'gender': profile.get_gender_display(),
            'email': profile.email,
            'profile_name': profile.category.name,
        },
        'service_rides': service_rides,
        'form': form,  # Pass the form to the template context
    }
    return render(request, 'wnApp/dashboard_rider.html', context)

@login_required
def dashboard_owner(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    if profile.category.name != 'Owner':
        return render(request, 'wnApp/dashboard_error.html')  # Display error page if user's category is not Owner
    user_data = {
        'username': user.username,
        'name': profile.name,
        'birth_date': profile.birth_date,
        'gender': profile.get_gender_display(),
        'email': profile.email,
        'profile_name': profile.category.name,
    }
    rental_properties = RentalProperty.objects.filter(owner=request.user)
    return render(request, 'wnApp/dashboard_owner.html', {'user_data': user_data, 'user_data': request.user.profile, 'rental_properties': rental_properties})

@login_required
def dashboard_tenant(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    if profile.category.name != 'Tenant':
        return render(request, 'wnApp/dashboard_error.html')  # Display error page if user's category is not Tenant
    user_data = {
        'username': user.username,
        'name': profile.name,
        'birth_date': profile.birth_date,
        'gender': profile.get_gender_display(),
        'email': profile.email,
        'profile_name': profile.category.name,
    }
    rental_properties = RentalProperty.objects.filter(is_available=True)
    return render(request, 'wnApp/dashboard_tenant.html', {'user_data': user_data, 'user_data': request.user.profile, 'rental_properties': rental_properties})

@login_required
def your_profile(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    form = ProfileForm(request.POST or None, instance=profile)
    
    if request.method == 'POST':
        if form.is_valid():
            form.save()

    return render(request, 'wnApp/your_profile.html', {'profile': profile, 'form': form})

#-------------------------------
def view_requests(request):
    ride_requests = RideRequest.objects.filter(service_ride__driver=request.user.profile)
    return render(request, 'wnApp/view_requests.html', {'ride_requests': ride_requests})

def view_available_service_rides(request):
    service_rides = ServiceRide.objects.filter(status='Available')
    return render(request, 'wnApp/view_available_service_rides.html', {'service_rides': service_rides})

def send_request(request, ride_id):
    if request.method == 'POST':
        ride = get_object_or_404(ServiceRide, id=ride_id)
        ride_request = RideRequest.objects.create(rider=request.user.profile, service_ride=ride)
        messages.success(request, 'Your request has been sent successfully.')
        return redirect('request_confirmation')

def request_detail(request, request_id):
    request_detail = get_object_or_404(RideRequest, id=request_id)
    return render(request, 'wnApp/request_detail.html', {'request_detail': request_detail})

def approve_request(request, request_id):
    ride_request = get_object_or_404(RideRequest, id=request_id)
    ride_request.status = 'Approved'
    ride_request.save()
    return redirect('request_detail', request_id=request_id)

def reject_request(request, request_id):
    ride_request = get_object_or_404(RideRequest, id=request_id)
    ride_request.status = 'Rejected'
    ride_request.save()
    return redirect('request_detail', request_id=request_id)

def request_confirmation(request):
    return render(request, 'wnApp/request_confirmation.html')
    
@login_required
def post_service_ride(request):
    if request.method == 'POST':
        form = ServiceRideForm(request.POST)
        if form.is_valid():
            service_ride = form.save(commit=False)
            service_ride.driver = request.user.profile
            service_ride.save()
            messages.success(request, 'Service ride posted successfully.')
            return redirect('dashboard_driver')
    else:
        form = ServiceRideForm()
    return render(request, 'wnApp/dashboard_driver.html', {'form': form})

@login_required
def view_service_rides(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    if profile.category.name != 'Driver':
        return render(request, 'wnApp/dashboard_error.html')  # Display error page if user's category is not Driver
    service_rides = ServiceRide.objects.filter(driver=profile)
    return render(request, 'wnApp/view_service_rides.html', {'service_rides': service_rides})






# views.py
@login_required
def post_rental_property(request):
    if request.method == 'POST':
        form = RentalPropertyForm(request.POST, request.FILES)
        if form.is_valid():
            rental_property = form.save(commit=False)
            rental_property.owner = request.user
            rental_property.save()
            return redirect('dashboard_owner')
    else:
        form = RentalPropertyForm()
    return render(request, 'wnApp/post_rental_property.html', {'form': form})

@login_required
def view_rental_properties(request):
    rental_properties = RentalProperty.objects.filter(owner=request.user)
    return render(request, 'wnApp/view_rental_properties.html', {'rental_properties': rental_properties})

@login_required
def apply_for_property(request, property_id):
    rental_property = RentalProperty.objects.get(pk=property_id)
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.tenant = request.user
            application.rental_property = rental_property
            application.save()
            return redirect('dashboard_tenant')
    else:
        form = ApplicationForm()
    return render(request, 'wnApp/apply_for_property.html', {'form': form})

@login_required
def view_applications(request):
    if request.user.profile.category.name == 'Tenant':
        applications = Application.objects.filter(tenant=request.user)
    else:
        rental_properties = RentalProperty.objects.filter(owner=request.user)
        applications = Application.objects.filter(rental_property__in=rental_properties)
    return render(request, 'wnApp/view_applications.html', {'applications': applications})


@login_required
def handle_application(request, application_id):
    application = Application.objects.get(pk=application_id)
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'Approve':
            application.status = 'Approved'
            application.save()
        elif action == 'Reject':
            application.status = 'Rejected'
            application.save()
    return redirect('view_applications')








'''#----------------------------------------------------------------------------------------------------------------------
def view_requests(request):
    staying_requests = StayingRequest.objects.filter(service_owner__owner=request.user.profile)
    return render(request, 'wnApp/view_requests.html', {'staying_requests': staying_requests})

def view_available_service_stayings(request):
    service_owner = ServiceOwner.objects.filter(status='Available')
    return render(request, 'wnApp/view_available_service_rides.html', {'service_stayings': service_owner})

def send_request(request, staying_id):
    if request.method == 'POST':
        staying = get_object_or_404(ServiceOwner, id=staying_id)
        staying_request = StayingRequest.objects.create(owner=request.user.profile, service_owner=staying)
        messages.success(request, 'Your request has been sent successfully.')
        return redirect('request_confirmation')

def request_detail(request, request_id):
    request_detail = get_object_or_404(StayingRequest, id=request_id)
    return render(request, 'wnApp/request_detail.html', {'request_detail': request_detail})

def approve_request(request, request_id):
    staying_request = get_object_or_404(StayingRequest, id=request_id)
    staying_request.status = 'Approved'
    staying_request.save()
    return redirect('request_detail', request_id=request_id)

def reject_request(request, request_id):
    staying_request = get_object_or_404(StayingRequest, id=request_id)
    staying_request.status = 'Rejected'
    staying_request.save()
    return redirect('request_detail', request_id=request_id)

def request_confirmation(request):
    return render(request, 'wnApp/request_confirmation.html')
    
@login_required
def post_service_staying(request):
    if request.method == 'POST':
        form = ServiceOwnerForm(request.POST)
        if form.is_valid():
            service_owner = form.save(commit=False)
            service_owner.owner = request.user.profile
            service_owner.save()
            messages.success(request, 'Service ride posted successfully.')
            return redirect('dashboard_owner')
    else:
        form = ServiceOwnerForm()
    return render(request, 'wnApp/post_service_ride.html', {'form': form})

@login_required
def view_service_stayings(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    if profile.category.name != 'Owner':
        return render(request, 'wnApp/dashboard_error.html')  # Display error page if user's category is not Driver
    service_stayings = ServiceOwner.objects.filter(owner=profile)
    return render(request, 'wnApp/view_service_rides.html', {'service_stayings': service_stayings})'''








#----------------------------------------------------------
'''def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            name = form.save()
            email = form.cleaned_data.get('email')
            message = form.cleaned_data.get('message')
            messages.success(request, 'Your message has been submitted successfully.')
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def contact_success_view(request):
    return render(request, 'contact_success.html')'''

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        # Create a ContactSubmission object and save it to the database
        submission = ContactSubmission(name=name, email=email, message=message)
        submission.save()
        
        # Optionally, you can also send an email notification or perform any other action here
        
        # Display a success message
        messages.success(request, 'Your message has been submitted successfully!')

        # Redirect to a success page or any other page as needed
        return redirect('contact')  # Change 'contact' to the appropriate URL name if needed
    else:
        return render(request, 'wnApp/contact.html')