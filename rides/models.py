from django.db import models

# Create your models here.
from django.db import models


class Driver(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class Passenger(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class Ride(models.Model):
    STATUS_CHOICES = [
        ('requested', 'Requested'),
        ('ongoing', 'Ongoing'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

    ride_id = models.CharField(max_length=20, unique=True)
    pickup_location = models.CharField(max_length=200)
    drop_location = models.CharField(max_length=200)

    driver = models.ForeignKey(
        Driver,
        on_delete=models.CASCADE,
        related_name='rides'
    )

    passenger = models.ForeignKey(
        Passenger,
        on_delete=models.CASCADE,
        related_name='rides'
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='requested'
    )

    fare = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ride_id