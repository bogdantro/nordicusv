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
    message = models.TextField(blank=True)
    price = models.FloatField(max_length=300, default=0)
    route_cords = models.TextField(blank=True)
    # Time
    onetime = models.BooleanField(default=True)
    onetime_time = models.DateTimeField(blank=True, null=True)
    interval = models.BooleanField(default=False)
    # Interval days
    date_start = models.DateField(blank=True, null=True)
    date_end = models.DateField(blank=True, null=True)
    monday = models.TimeField(blank=True, null=True)
    tuesday = models.TimeField(blank=True, null=True)
    wednesday = models.TimeField(blank=True, null=True)
    thursday = models.TimeField(blank=True, null=True)
    friday = models.TimeField(blank=True, null=True)
    saturday = models.TimeField(blank=True, null=True)
    sunday = models.TimeField(blank=True, null=True)
    choose_interval = models.CharField(max_length=500, blank=True)
    # Custom Cords
    custom_cords_1 = models.CharField(max_length=1000, blank=True)
    custom_cords_2 = models.CharField(max_length=1000, blank=True)
    custom_cords_3 = models.CharField(max_length=1000, blank=True)
    custom_cords_4 = models.CharField(max_length=1000, blank=True)
    custom_cords_5 = models.CharField(max_length=1000, blank=True)
    custom_cords_6 = models.CharField(max_length=1000, blank=True)
    custom_cords_7 = models.CharField(max_length=1000, blank=True)
    custom_cords_8 = models.CharField(max_length=1000, blank=True)
    custom_cords_9 = models.CharField(max_length=1000, blank=True)
    custom_cords_10 = models.CharField(max_length=1000, blank=True)
    custom_cords_11 = models.CharField(max_length=1000, blank=True)
    custom_cords_12 = models.CharField(max_length=1000, blank=True)
    custom_cords_13 = models.CharField(max_length=1000, blank=True)
    custom_cords_14 = models.CharField(max_length=1000, blank=True)
    custom_cords_15 = models.CharField(max_length=1000, blank=True)
    custom_cords_16 = models.CharField(max_length=1000, blank=True)
    custom_cords_17 = models.CharField(max_length=1000, blank=True)
    custom_cords_18 = models.CharField(max_length=1000, blank=True)
    custom_cords_19 = models.CharField(max_length=1000, blank=True)
    custom_cords_20 = models.CharField(max_length=1000, blank=True)
    custom_cords_21 = models.CharField(max_length=1000, blank=True)
    custom_cords_22 = models.CharField(max_length=1000, blank=True)
    custom_cords_23 = models.CharField(max_length=1000, blank=True)
    custom_cords_24 = models.CharField(max_length=1000, blank=True)
    custom_cords_25 = models.CharField(max_length=1000, blank=True)
    custom_cords_26 = models.CharField(max_length=1000, blank=True)
    custom_cords_27 = models.CharField(max_length=1000, blank=True)
    custom_cords_28 = models.CharField(max_length=1000, blank=True)
    custom_cords_29 = models.CharField(max_length=1000, blank=True)
    custom_cords_30 = models.CharField(max_length=1000, blank=True)
    custom_cords_31 = models.CharField(max_length=1000, blank=True)
    custom_cords_32 = models.CharField(max_length=1000, blank=True)
    custom_cords_33 = models.CharField(max_length=1000, blank=True)
    custom_cords_34 = models.CharField(max_length=1000, blank=True)
    custom_cords_35 = models.CharField(max_length=1000, blank=True)
    custom_cords_36 = models.CharField(max_length=1000, blank=True)
    custom_cords_37 = models.CharField(max_length=1000, blank=True)
    custom_cords_38 = models.CharField(max_length=1000, blank=True)
    custom_cords_39 = models.CharField(max_length=1000, blank=True)
    custom_cords_40 = models.CharField(max_length=1000, blank=True)
    
    # Sensors
    waypoint_1_sensor = models.CharField(max_length=1000, blank=True)
    waypoint_1_sensor_depth = models.CharField(max_length=1000, blank=True)
    waypoint_1_sensor_message = models.TextField(blank=True)

    waypoint_2_sensor = models.CharField(max_length=1000, blank=True)
    waypoint_2_sensor_depth = models.CharField(max_length=1000, blank=True)
    waypoint_2_sensor_message = models.TextField(blank=True)

    waypoint_3_sensor = models.CharField(max_length=1000, blank=True)
    waypoint_3_sensor_depth = models.CharField(max_length=1000, blank=True)
    waypoint_3_sensor_message = models.TextField(blank=True)

    waypoint_4_sensor = models.CharField(max_length=1000, blank=True)
    waypoint_4_sensor_depth = models.CharField(max_length=1000, blank=True)
    waypoint_4_sensor_message = models.TextField(blank=True)

    waypoint_5_sensor = models.CharField(max_length=1000, blank=True)
    waypoint_5_sensor_depth = models.CharField(max_length=1000, blank=True)
    waypoint_5_sensor_message = models.TextField(blank=True)

    waypoint_6_sensor = models.CharField(max_length=1000, blank=True)
    waypoint_6_sensor_depth = models.CharField(max_length=1000, blank=True)
    waypoint_6_sensor_message = models.TextField(blank=True)

    waypoint_7_sensor = models.CharField(max_length=1000, blank=True)
    waypoint_7_sensor_depth = models.CharField(max_length=1000, blank=True)
    waypoint_7_sensor_message = models.TextField(blank=True)

    waypoint_8_sensor = models.CharField(max_length=1000, blank=True)
    waypoint_8_sensor_depth = models.CharField(max_length=1000, blank=True)
    waypoint_8_sensor_message = models.TextField(blank=True)

    waypoint_9_sensor = models.CharField(max_length=1000, blank=True)
    waypoint_9_sensor_depth = models.CharField(max_length=1000, blank=True)
    waypoint_9_sensor_message = models.TextField(blank=True)

    waypoint_10_sensor = models.CharField(max_length=1000, blank=True)
    waypoint_10_sensor_depth = models.CharField(max_length=1000, blank=True)
    waypoint_10_sensor_message = models.TextField(blank=True)

    waypoint_11_sensor = models.CharField(max_length=1000, blank=True)
    waypoint_11_sensor_depth = models.CharField(max_length=1000, blank=True)
    waypoint_11_sensor_message = models.TextField(blank=True)

    waypoint_12_sensor = models.CharField(max_length=1000, blank=True)
    waypoint_12_sensor_depth = models.CharField(max_length=1000, blank=True)
    waypoint_12_sensor_message = models.TextField(blank=True)

    waypoint_13_sensor = models.CharField(max_length=1000, blank=True)
    waypoint_13_sensor_depth = models.CharField(max_length=1000, blank=True)
    waypoint_13_sensor_message = models.TextField(blank=True)

    waypoint_14_sensor = models.CharField(max_length=1000, blank=True)
    waypoint_14_sensor_depth = models.CharField(max_length=1000, blank=True)
    waypoint_14_sensor_message = models.TextField(blank=True)

    waypoint_15_sensor = models.CharField(max_length=1000, blank=True)
    waypoint_15_sensor_depth = models.CharField(max_length=1000, blank=True)
    waypoint_15_sensor_message = models.TextField(blank=True)

    waypoint_16_sensor = models.CharField(max_length=1000, blank=True)
    waypoint_16_sensor_depth = models.CharField(max_length=1000, blank=True)
    waypoint_16_sensor_message = models.TextField(blank=True)

    waypoint_17_sensor = models.CharField(max_length=1000, blank=True)
    waypoint_17_sensor_depth = models.CharField(max_length=1000, blank=True)
    waypoint_17_sensor_message = models.TextField(blank=True)

    waypoint_18_sensor = models.CharField(max_length=1000, blank=True)
    waypoint_18_sensor_depth = models.CharField(max_length=1000, blank=True)
    waypoint_18_sensor_message = models.TextField(blank=True)

    waypoint_19_sensor = models.CharField(max_length=1000, blank=True)
    waypoint_19_sensor_depth = models.CharField(max_length=1000, blank=True)
    waypoint_19_sensor_message = models.TextField(blank=True)

    waypoint_20_sensor = models.CharField(max_length=1000, blank=True)
    waypoint_20_sensor_depth = models.CharField(max_length=1000, blank=True)
    waypoint_20_sensor_message = models.TextField(blank=True)

    waypoint_21_sensor = models.CharField(max_length=1000, blank=True)
    waypoint_21_sensor_depth = models.CharField(max_length=1000, blank=True)
    waypoint_21_sensor_message = models.TextField(blank=True)

    waypoint_22_sensor = models.CharField(max_length=1000, blank=True)
    waypoint_22_sensor_depth = models.CharField(max_length=1000, blank=True)
    waypoint_22_sensor_message = models.TextField(blank=True)

    waypoint_23_sensor = models.CharField(max_length=1000, blank=True)
    waypoint_23_sensor_depth = models.CharField(max_length=1000, blank=True)
    waypoint_23_sensor_message = models.TextField(blank=True)

    waypoint_24_sensor = models.CharField(max_length=1000, blank=True)
    waypoint_24_sensor_depth = models.CharField(max_length=1000, blank=True)
    waypoint_24_sensor_message = models.TextField(blank=True)

    waypoint_25_sensor = models.CharField(max_length=1000, blank=True)
    waypoint_25_sensor_depth = models.CharField(max_length=1000, blank=True)
    waypoint_25_sensor_message = models.TextField(blank=True)

    waypoint_26_sensor = models.CharField(max_length=1000, blank=True)
    waypoint_26_sensor_depth = models.CharField(max_length=1000, blank=True)
    waypoint_26_sensor_message = models.TextField(blank=True)

    waypoint_27_sensor = models.CharField(max_length=1000, blank=True)
    waypoint_27_sensor_depth = models.CharField(max_length=1000, blank=True)
    waypoint_27_sensor_message = models.TextField(blank=True)

    waypoint_28_sensor = models.CharField(max_length=1000, blank=True)
    waypoint_28_sensor_depth = models.CharField(max_length=1000, blank=True)
    waypoint_28_sensor_message = models.TextField(blank=True)

    waypoint_29_sensor = models.CharField(max_length=1000, blank=True)
    waypoint_29_sensor_depth = models.CharField(max_length=1000, blank=True)
    waypoint_29_sensor_message = models.TextField(blank=True)

    waypoint_30_sensor = models.CharField(max_length=1000, blank=True)
    waypoint_30_sensor_depth = models.CharField(max_length=1000, blank=True)
    waypoint_30_sensor_message = models.TextField(blank=True)

    waypoint_31_sensor = models.CharField(max_length=1000, blank=True)
    waypoint_31_sensor_depth = models.CharField(max_length=1000, blank=True)
    waypoint_31_sensor_message = models.TextField(blank=True)

    waypoint_32_sensor = models.CharField(max_length=1000, blank=True)
    waypoint_32_sensor_depth = models.CharField(max_length=1000, blank=True)
    waypoint_32_sensor_message = models.TextField(blank=True)

    waypoint_33_sensor = models.CharField(max_length=1000, blank=True)
    waypoint_33_sensor_depth = models.CharField(max_length=1000, blank=True)
    waypoint_33_sensor_message = models.TextField(blank=True)

    waypoint_34_sensor = models.CharField(max_length=1000, blank=True)
    waypoint_34_sensor_depth = models.CharField(max_length=1000, blank=True)
    waypoint_34_sensor_message = models.TextField(blank=True)

    waypoint_35_sensor = models.CharField(max_length=1000, blank=True)
    waypoint_35_sensor_depth = models.CharField(max_length=1000, blank=True)
    waypoint_35_sensor_message = models.TextField(blank=True)

    waypoint_36_sensor = models.CharField(max_length=1000, blank=True)
    waypoint_36_sensor_depth = models.CharField(max_length=1000, blank=True)
    waypoint_36_sensor_message = models.TextField(blank=True)

    waypoint_37_sensor = models.CharField(max_length=1000, blank=True)
    waypoint_37_sensor_depth = models.CharField(max_length=1000, blank=True)
    waypoint_37_sensor_message = models.TextField(blank=True)

    waypoint_38_sensor = models.CharField(max_length=1000, blank=True)
    waypoint_38_sensor_depth = models.CharField(max_length=1000, blank=True)
    waypoint_38_sensor_message = models.TextField(blank=True)

    waypoint_39_sensor = models.CharField(max_length=1000, blank=True)
    waypoint_39_sensor_depth = models.CharField(max_length=1000, blank=True)
    waypoint_39_sensor_message = models.TextField(blank=True)

    waypoint_40_sensor = models.CharField(max_length=1000, blank=True)
    waypoint_40_sensor_depth = models.CharField(max_length=1000, blank=True)
    waypoint_40_sensor_message = models.TextField(blank=True)
    
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