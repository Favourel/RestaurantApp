from django import forms
from .models import Reservation


class ReservationForm(forms.ModelForm):

    class Meta:
        model = Reservation
        fields = [
            "full_name", "phone", "email", "people", "check_in_date", "check_in_time"
        ]