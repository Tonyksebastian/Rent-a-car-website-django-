from django.shortcuts import render
from .models import car
from .forms import Bookingform

def index(request):
    dict_car={'name': car.objects.all() }
    return render (request,'cars.html',dict_car)

def indexone(request):
    if request.method == "POST":
        form=Bookingform(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'confirm.html')
    form=Bookingform()
    dict_Book={'form': form }
    return render (request,'Booking.html',dict_Book)



 
