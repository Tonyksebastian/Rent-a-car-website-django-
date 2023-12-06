from django import forms
from .models import Booking

class DateInput(forms.DateInput):
        input_type='date'
class Bookingform(forms.ModelForm):
    
    class Meta:
        model=Booking
        fields='__all__'
        widgets={
             'bookingdate':DateInput()
                }

        labels={
             'cname': "Name",
             'cphone': "Phone No",
             'cemail': "Email",
             'carname': "Model",
             'bookingdate': "Date of Booking"
        }