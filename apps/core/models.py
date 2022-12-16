from django.db import models
from datetime import date
from django.contrib.auth.models import User
from django.utils import tree

class Order(models.Model):
    # User info
    user = models.ForeignKey(User, related_name='orders', on_delete=models.SET_NULL, blank=True, null=True)
    user_html = models.CharField(max_length=100, blank=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    # Survey info
    message = models.CharField(max_length=700, blank=True)
    price = models.FloatField(max_length=300, default=0)
    time = models.DateTimeField(blank=False)
    route_cords = models.TextField(blank=True)
    custom_cords = models.TextField(blank=True)
    # Sensors
    sensor_1_waypoins = models.TextField()
    sensor_1_depth = models.TextField()
    # Admin
    created_at = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)
    is_finished = models.BooleanField(default=False)
    is_confirmed = models.BooleanField(default=False)
    status_1 = models.BooleanField(default=False)
    status_2 = models.BooleanField(default=False)
    status_3 = models.BooleanField(default=False)
    status_4 = models.BooleanField(default=False)
    status_5 = models.BooleanField(default=False)


    def __str__(self):
        return self.name