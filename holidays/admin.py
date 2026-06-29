from django.contrib import admin
from django.utils.html import format_html
from .models import Inquiry, GroupTrip, GroupBooking, CollegeCoordinator, Transport


@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'tour_type',
        'destination',
        'destination_country',
        'phone',
        'number_of_people',
        'total_budget',
        'travel_mode',
        'created_at',
    )
    list_filter = ('tour_type', 'travel_mode', 'created_at')
    search_fields = ('name', 'phone', 'destination', 'destination_country', 'institution_name')
    ordering = ('-created_at',)


@admin.register(GroupTrip)
class GroupTripAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'destination', 'price', 'departure_date', 'available_seats', 'is_active', 'cover_photo_preview')
    list_filter = ('category', 'departure_date', 'is_active')
    search_fields = ('title', 'description', 'category', 'destination')
    readonly_fields = ('cover_photo_preview',)

    fieldsets = (
        (None, {
            'fields': ('title', 'category', 'cover_photo', 'cover_photo_preview', 'destination', 'price', 'description', 'duration', 'departure_date', 'available_seats', 'facilities', 'is_active')
        }),
    )

    def cover_photo_preview(self, obj):
        if obj.cover_photo:
            return format_html('<img src="{}" style="max-width: 200px; max-height: 120px; border-radius: 12px;" />', obj.cover_photo.url)
        return '(No image)'
    cover_photo_preview.short_description = 'Cover Photo Preview'


@admin.register(GroupBooking)
class GroupBookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'trip', 'phone', 'number_of_people', 'booked_on')
    list_filter = ('trip__category', 'booked_on')
    search_fields = ('name', 'phone', 'trip__title')
    ordering = ('-booked_on',)


admin.site.register(CollegeCoordinator)
admin.site.register(Transport)