from django.db import models


# Create your models here.
class car(models.Model):
    carimg=models.ImageField(upload_to='pic')
    carname=models.CharField(max_length=60)
    carDesi=models.CharField(max_length=60)
    carPrice=models.CharField(max_length=30)

    def __str__(self):
        return self.carname 
    
class Booking(models.Model):
        cname=models.CharField(max_length=60)
        cphone=models.CharField(max_length=60)
        cemail=models.CharField(max_length=60)
        carname=models.ForeignKey(car,on_delete=models.CASCADE)
        bookingdate=models.DateField()