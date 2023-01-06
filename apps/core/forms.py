from django.db.models import fields
from django import forms
from .models import Order
from django.db import models



class Order(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(Order, self).__init__(*args, **kwargs)

    class Meta:
        model = Order
        fields = (
        'name', 'email', 'message', 'route_cords', 'onetime', 'onetime_time', 'interval', 'user_html',
        # Interval
        'date_start',
        'date_end',
        'monday',
        'tuesday',
        'wednesday',
        'thursday',
        'friday',
        'saturday',
        'sunday',
        'choose_interval',
        # Cords
        'custom_cords_1',
        'custom_cords_2',
        'custom_cords_3',
        'custom_cords_4',
        'custom_cords_5',
        'custom_cords_6',
        'custom_cords_7',
        'custom_cords_8',
        'custom_cords_9',
        'custom_cords_10',
        # Waypoints
        'waypoint_1_sensor', 'waypoint_1_sensor_depth', 'waypoint_1_sensor_message',
        'waypoint_2_sensor', 'waypoint_2_sensor_depth', 'waypoint_2_sensor_message',
        'waypoint_3_sensor', 'waypoint_3_sensor_depth', 'waypoint_3_sensor_message',
        'waypoint_4_sensor', 'waypoint_4_sensor_depth', 'waypoint_4_sensor_message',
        'waypoint_5_sensor', 'waypoint_5_sensor_depth', 'waypoint_5_sensor_message',
        'waypoint_6_sensor', 'waypoint_6_sensor_depth', 'waypoint_6_sensor_message',
        'waypoint_7_sensor', 'waypoint_7_sensor_depth', 'waypoint_7_sensor_message',
        'waypoint_8_sensor', 'waypoint_8_sensor_depth', 'waypoint_8_sensor_message',
        'waypoint_9_sensor', 'waypoint_9_sensor_depth', 'waypoint_9_sensor_message',
        'waypoint_10_sensor', 'waypoint_10_sensor_depth', 'waypoint_10_sensor_message',
        )