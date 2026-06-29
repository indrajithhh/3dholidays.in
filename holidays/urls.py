from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('college/', views.college, name='college'),
    path('pilgrimage/', views.pilgrimage, name='pilgrimage'),
    path('domestic/', views.domestic, name='domestic'),
    path('international/', views.international, name='international'),
    path('group-trips/', views.packages, name='group_trips'),
    path('packages/', views.packages, name='packages'),
    path('package/<int:trip_id>/', views.package_detail, name='package_detail'),
    path('book-trip/<int:trip_id>/', views.book_trip, name='book_trip'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('thank-you/', views.thank_you, name='thank_you'),
]
