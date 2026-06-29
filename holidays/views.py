from django.shortcuts import render, redirect, get_object_or_404

from .models import Inquiry, QuickInquiry, GroupTrip
from .forms import InquiryForm, QuickInquiryForm, GroupBookingForm


def home(request):
    if request.method == 'POST':
        form = QuickInquiryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thank_you')
    else:
        form = QuickInquiryForm()

    return render(request, 'home.html', {'quick_form': form})


def _save_inquiry(request, tour_type, template_name):
    if request.method == 'POST':
        form = InquiryForm(request.POST, tour_type=tour_type)
        if form.is_valid():
            inquiry = form.save(commit=False)
            inquiry.tour_type = tour_type
            inquiry.save()
            return redirect('thank_you')
    else:
        form = InquiryForm(tour_type=tour_type)

    return render(request, template_name, {'form': form, 'tour_type': tour_type})


def college(request):
    return _save_inquiry(request, 'College', 'college.html')


def pilgrimage(request):
    return _save_inquiry(request, 'Pilgrimage', 'pilgrimage.html')


def domestic(request):
    return _save_inquiry(request, 'Domestic', 'domestic.html')


def international(request):
    return _save_inquiry(request, 'International', 'international.html')


def packages(request):
    trips = GroupTrip.objects.filter(is_active=True)
    return render(request, 'group_trips.html', {'trips': trips})


def package_detail(request, trip_id):
    trip = get_object_or_404(GroupTrip, id=trip_id, is_active=True)
    return render(request, 'package_detail.html', {'trip': trip})


def book_trip(request, trip_id):
    trip = get_object_or_404(GroupTrip, id=trip_id, is_active=True)
    if request.method == 'POST':
        form = GroupBookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.trip = trip
            booking.save()
            return redirect('thank_you')
    else:
        form = GroupBookingForm()

    return render(request, 'book_trip.html', {'trip': trip, 'form': form})


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def thank_you(request):
    return render(request, 'thank_you.html')
