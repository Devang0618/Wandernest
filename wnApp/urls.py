from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('riding/', views.riding, name='riding'),
    path('staying/', views.staying, name='staying'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('dashboard/driver/', views.dashboard_driver, name='dashboard_driver'),
    path('dashboard/rider/', views.dashboard_rider, name='dashboard_rider'),
    path('dashboard/owner/', views.dashboard_owner, name='dashboard_owner'),
    path('dashboard/tenant/', views.dashboard_tenant, name='dashboard_tenant'),
    path('your-profile/', views.your_profile, name='your_profile'),
    path('dashboard/driver/post-ride/', views.post_service_ride, name='post_service_ride'),
    path('dashboard/driver/view-rides/', views.view_service_rides, name='view_service_rides'),
    path('dashboard/driver/requests/', views.view_requests, name='view_requests'),
    path('dashboard/rider/available-rides/', views.view_available_service_rides, name='view_available_service_rides'),
    path('dashboard/rider/request-confirmation/', views.request_confirmation, name='request_confirmation'),
    path('dashboard/driver/requests/<int:request_id>/', views.request_detail, name='request_detail'),
    path('dashboard/driver/requests/<int:request_id>/approve/', views.approve_request, name='approve_request'),
    path('dashboard/driver/requests/<int:request_id>/reject/', views.reject_request, name='reject_request'),
    path('dashboard/rider/send-request/<int:ride_id>/', views.send_request, name='send_request'),

    # New URLs for Owner and Tenant
    path('dashboard/owner/', views.dashboard_owner, name='dashboard_owner'),
    path('dashboard/tenant/', views.dashboard_tenant, name='dashboard_tenant'),
    path('post-rental-property/', views.post_rental_property, name='post_rental_property'),
    path('view-rental-properties/', views.view_rental_properties, name='view_rental_properties'),
    path('apply-for-property/<int:property_id>/', views.apply_for_property, name='apply_for_property'),
    path('view-applications/', views.view_applications, name='view_applications'),
    path('handle-application/<int:application_id>/', views.handle_application, name='handle_application'),
    #path('contact/success/', views.contact_success_view, name='contact_success'),
]
