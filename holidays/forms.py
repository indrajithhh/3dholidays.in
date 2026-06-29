from django import forms
from .models import Inquiry, QuickInquiry
from .models import GroupBooking


class InquiryForm(forms.ModelForm):
    class Meta:
        model = Inquiry
        fields = [
            'name',
            'phone',
            'destination',
            'destination_country',
            'number_of_people',
            'travel_mode',
            'total_budget',
            'institution_name',
        ]
        widgets = {
            'destination': forms.TextInput(attrs={'placeholder': 'Destination'}),
            'destination_country': forms.TextInput(attrs={'placeholder': 'Destination Country'}),
            'number_of_people': forms.NumberInput(attrs={'min': 1}),
            'total_budget': forms.NumberInput(attrs={'step': '0.01'}),
            'institution_name': forms.TextInput(attrs={'placeholder': 'College or Group Name'}),
        }

    def __init__(self, *args, tour_type=None, **kwargs):
        super().__init__(*args, **kwargs)
        if tour_type in {'Domestic', 'Pilgrimage', 'College'}:
            self.fields.pop('destination_country', None)
        if tour_type in {'Domestic', 'International', 'Pilgrimage'}:
            self.fields.pop('institution_name', None)


class QuickInquiryForm(forms.ModelForm):
    class Meta:
        model = QuickInquiry
        fields = ['name', 'phone', 'tour_type']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Full Name'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Mobile Number'}),
            'tour_type': forms.Select(),
        }


class GroupBookingForm(forms.ModelForm):
    class Meta:
        model = GroupBooking
        fields = ['name', 'phone', 'number_of_people']
        widgets = {
            'number_of_people': forms.NumberInput(attrs={'min': 1}),
        }