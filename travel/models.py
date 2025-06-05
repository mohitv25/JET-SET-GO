from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class contact(models.Model):
    name = models.CharField(max_length=120, default='')
    email = models.CharField(max_length=100)
    subject = models.CharField(max_length=120, default='')
    message = models.TextField()
    date = models.DateField()
    
    def __str__(self):
        return self.name    
    
class Itinerary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    destination = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    names = models.TextField()  # Comma-separated list of names
    num_people = models.PositiveIntegerField()
    activities = models.TextField()

    def __str__(self):
        return f"{self.destination} ({self.start_date} to {self.end_date})"
class Country(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    
class TouristLocation(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    description = models.TextField()
    def __str__(self):
        return self.name

class GroupBooking(models.Model):
    destination = models.ForeignKey(TouristLocation, on_delete=models.CASCADE)
    arrival_date = models.DateField(default=None)
    departure_date = models.DateField(default=None)
    total_participants = models.IntegerField()
    group_name = models.CharField(max_length=100, default=None)  # New field: Group Name


class BookingHistory(models.Model):
    total_members = models.IntegerField()
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
# SQL View for active group 
class ActiveGroupBookings(models.Model):
    class Meta:
        managed = False
        db_table = 'active_group_bookings'
    destination = models.CharField(max_length=100)
    departure_date = models.DateField()
    total_participants = models.IntegerField()

# SQL Trigger for notifications
# Example: Send email notification when a new group booking is created
class NewGroupBookingTrigger(models.Model):
    class Meta:
        managed = False
        db_table = 'new_group_booking_trigger'

