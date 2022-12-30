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
    route_cords = models.TextField(blank=True)
    # Time
    onetime = models.BooleanField(default=True)
    onetime_time = models.DateTimeField(blank=False)
    interval = models.BooleanField(default=False)
    interval_time = models.DateTimeField(blank=False)
    # Custom Cords
    custom_cords_1 = models.CharField(max_length=1000)
    custom_cords_2 = models.CharField(max_length=1000)
    custom_cords_3 = models.CharField(max_length=1000)
    custom_cords_4 = models.CharField(max_length=1000)
    custom_cords_5 = models.CharField(max_length=1000)
    custom_cords_6 = models.CharField(max_length=1000)
    custom_cords_7 = models.CharField(max_length=1000)
    custom_cords_8 = models.CharField(max_length=1000)
    custom_cords_9 = models.CharField(max_length=1000)
    custom_cords_10 = models.CharField(max_length=1000)
    
    # Sensors
    # Waypoint 1
    waypoint_1_sensor = models.CharField(max_length=1000)
    waypoint_1_sensor_depth = models.CharField(max_length=1000)
    waypoint_1_sensor_message = models.TextField()

    # Waypoint 2
    waypoint_2_sensor = models.CharField(max_length=1000)
    waypoint_2_sensor_depth = models.CharField(max_length=1000)
    waypoint_2_sensor_message = models.TextField()

    # Waypoint 3
    waypoint_3_sensor = models.CharField(max_length=1000)
    waypoint_3_sensor_depth = models.CharField(max_length=1000)
    waypoint_3_sensor_message = models.TextField()

    # Waypoint 4
    waypoint_4_sensor = models.CharField(max_length=1000)
    waypoint_4_sensor_depth = models.CharField(max_length=1000)
    waypoint_4_sensor_message = models.TextField()

    # Waypoint 5
    waypoint_5_sensor = models.CharField(max_length=1000)
    waypoint_5_sensor_depth = models.CharField(max_length=1000)
    waypoint_5_sensor_message = models.TextField()

    # Waypoint 6
    waypoint_6_sensor = models.CharField(max_length=1000)
    waypoint_6_sensor_depth = models.CharField(max_length=1000)
    waypoint_6_sensor_message = models.TextField()

    # Waypoint 7
    waypoint_7_sensor = models.CharField(max_length=1000)
    waypoint_7_sensor_depth = models.CharField(max_length=1000)
    waypoint_7_sensor_message = models.TextField()

    # Waypoint 8
    waypoint_8_sensor = models.CharField(max_length=1000)
    waypoint_8_sensor_depth = models.CharField(max_length=1000)
    waypoint_8_sensor_message = models.TextField()

    # Waypoint 9
    waypoint_9_sensor = models.CharField(max_length=1000)
    waypoint_9_sensor_depth = models.CharField(max_length=1000)
    waypoint_9_sensor_message = models.TextField()

    # Waypoint 10
    waypoint_10_sensor = models.CharField(max_length=1000)
    waypoint_10_sensor_depth = models.CharField(max_length=1000)
    waypoint_10_sensor_message = models.TextField()
    
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