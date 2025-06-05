from django import forms
from travel.models import Country,GroupBooking, BookingHistory

class CountrySelectForm(forms.Form):
    country = forms.ModelChoiceField(queryset=Country.objects.all())


class GroupBookingForm(forms.ModelForm):
    class Meta:
        model = GroupBooking
        fields = ['group_name', 'destination', 'arrival_date', 'departure_date', 'total_participants']
        widgets = {
            'arrival_date': forms.DateInput(attrs={'type': 'date'}),
            'departure_date': forms.DateInput(attrs={'type': 'date'})
        }


class BookingHistoryForm(forms.ModelForm):
    class Meta:
        model = BookingHistory
        fields = [ 'total_members', 'amount_paid']