from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from datetime import datetime
from travel.models import contact, Itinerary, TouristLocation, GroupBooking, ActiveGroupBookings
from travel.forms import CountrySelectForm,GroupBookingForm, BookingHistoryForm
from django.contrib import messages
def home(request):
    return render(request, 'body.html')
def about(request):
    return render(request,'#about')
def services(request):
    return render(request,'#services')
def blog(request):
    return render(request, 'blog.html')
def portfolio(request):
    return render(request, 'portfolio.html')
def adventure(request):
    return render(request, 'adventure.html')
def team(request):
    return render(request, '#team')
def Contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        Contact = contact(name = name, email = email, subject = subject, message = message, date = datetime.today())
        Contact.save()
        messages.success(request, "")
    return render(request, 'body.html')



# Create your views here.

@login_required
def itinerary_planner(request):
    if request.method == 'POST':
        destination = request.POST.get('destination')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        names = request.POST.get('names')
        num_people = request.POST.get('num_people')
        activities = request.POST.get('activities')
        
        # Get the current authenticated user
        user = request.user

        # Create the itinerary associated with the current user
        itinerary = Itinerary.objects.create(
            user=user,
            destination=destination,
            start_date=start_date,
            end_date=end_date,
            names=names,
            num_people=num_people,
            activities=activities
        )
        messages.success(request, "Your planning is safe with us!")
        return redirect('/')  # Redirect to success page
    return render(request, 'planner.html')

def tourist_location_by_country(request):
    if request.method == 'POST':
        form = CountrySelectForm(request.POST)
        if form.is_valid():
            country_id = form.cleaned_data['country'].id
            tourist_locations = TouristLocation.objects.filter(country_id=country_id)
            return render(request, 'tourist_location_by_country.html', {'form': form, 'tourist_locations': tourist_locations})
    else:
        form = CountrySelectForm()
    return render(request, 'country_select.html', {'form': form})

def group_booking_management(request):
    # Retrieve active group bookings using SQL view
    active_bookings = ActiveGroupBookings.objects.all()

    # Add logic for handling user requests (e.g., creating, editing, deleting bookings)

    return render(request, 'group_booking_management.html', {'active_bookings': active_bookings})

@login_required
def itinerary_status(request):
    # Retrieve itinerary entries for the logged-in user
    itineraries = Itinerary.objects.filter(user=request.user)
    return render(request, 'itinerary_status.html', {'itineraries': itineraries})


def group_booking(request):
    if request.method == 'POST':
        booking_form = GroupBookingForm(request.POST)
        history_form = BookingHistoryForm(request.POST)

        if booking_form.is_valid() and history_form.is_valid():
            # Save group booking
            booking = booking_form.save()

            # Save booking history
            history = history_form.save(commit=False)
            history.group_booking = booking
            history.total_members = booking.total_participants
            history.save()
            messages.success(request,"Hope your group trip goes well!")
            return redirect('/')  # Redirect to success page
    else:
        booking_form = GroupBookingForm()
        history_form = BookingHistoryForm()

    return render(request, 'group_booking_form.html', {'booking_form': booking_form, 'history_form': history_form})