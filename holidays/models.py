from django.db import models

class Inquiry(models.Model):
    TOUR_TYPES = [
        ('College', 'College'),
        ('Pilgrimage', 'Pilgrimage'),
        ('Domestic', 'Domestic'),
        ('International', 'International'),
        ('Group Tour', 'Group Tour'),
    ]

    TRAVEL_MODES = [
        ('Bus', 'Bus'),
        ('Train', 'Train'),
        ('Flight', 'Flight'),
        ('Coach', 'Coach'),
        ('Other', 'Other'),
    ]

    tour_type = models.CharField(max_length=20, choices=TOUR_TYPES)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    destination = models.CharField(max_length=200)
    number_of_people = models.PositiveIntegerField(default=1)
    total_budget = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        blank=True,
        null=True
    )
    travel_mode = models.CharField(
        max_length=20,
        choices=TRAVEL_MODES,
        blank=True,
        null=True
    )
    institution_name = models.CharField(
        max_length=200,
        blank=True,
        null=True
    )
    destination_country = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.tour_type})"


class QuickInquiry(models.Model):
    TOUR_TYPES = Inquiry.TOUR_TYPES

    tour_type = models.CharField(max_length=20, choices=TOUR_TYPES)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.tour_type})"


class GroupTrip(models.Model):
    CATEGORY_CHOICES = [
        ('College', 'College'),
        ('Pilgrimage', 'Pilgrimage'),
        ('Domestic', 'Domestic'),
        ('International', 'International'),
        ('Group Tour', 'Group Tour'),
    ]

    title = models.CharField(max_length=200)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    cover_photo = models.ImageField(upload_to='group_trips/', blank=True, null=True)
    destination = models.CharField(max_length=200, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    duration = models.CharField(max_length=100, blank=True, null=True)
    departure_date = models.DateField(blank=True, null=True)
    available_seats = models.PositiveIntegerField(blank=True, null=True)
    facilities = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class GroupBooking(models.Model):
    trip = models.ForeignKey(GroupTrip, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    number_of_people = models.PositiveIntegerField(default=1)
    booked_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.trip.title}"


class CollegeCoordinator(models.Model):
    name = models.CharField(max_length=100)
    college_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.college_name


class Transport(models.Model):
    TRANSPORT_TYPES = [
        ('Bus', 'Bus'),
        ('Train', 'Train'),
        ('Flight', 'Flight'),
    ]

    trip = models.ForeignKey(
        GroupTrip,
        on_delete=models.CASCADE
    )

    transport_type = models.CharField(
        max_length=20,
        choices=TRANSPORT_TYPES
    )

    vehicle_name = models.CharField(max_length=100)

    number = models.CharField(max_length=50)

    departure = models.CharField(max_length=100)
    arrival = models.CharField(max_length=100)

    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()

    def __str__(self):
        return f"{self.transport_type} - {self.number}"