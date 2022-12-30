from django.contrib import admin
from .models import *




class OrderAdmin(admin.ModelAdmin):
    list_filter  = ['user']
    list_display =['id', 'name', 'user', 'created_at', 'paid']
    fieldsets = (
      ('User info', {
          'fields': ('user', 'user_html', 'name', 'email',)
      }),
      ('Survey info', {
          'fields': ('message', 'price',)
      }),
      ('Cordinates', {
          'fields': ('route_cords',)
      }),
      ('Custom cordinates', {
          'fields': (
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
          )
      }),
      ('Time', {
          'fields': ('time',)
      }),
      ('Waypoint 1 sensors', {
          'fields': (
            'waypoint_1_sensor',
            'waypoint_1_sensor_depth',
            'waypoint_1_sensor_message',
          )
      }),
      ('Waypoint 2 sensors', {
          'fields': (
            'waypoint_2_sensor',
            'waypoint_2_sensor_depth',
            'waypoint_2_sensor_message',
          )
      }),
      ('Waypoint 3 sensors', {
          'fields': (
            'waypoint_3_sensor',
            'waypoint_3_sensor_depth',
            'waypoint_3_sensor_message',
          )
      }),
      ('Waypoint 4 sensors', {
          'fields': (
            'waypoint_4_sensor',
            'waypoint_4_sensor_depth',
            'waypoint_4_sensor_message',
          )
      }),
      ('Waypoint 5 sensors', {
          'fields': (
            'waypoint_5_sensor',
            'waypoint_5_sensor_depth',
            'waypoint_5_sensor_message',
          )
      }),
      ('Waypoint 6 sensors', {
          'fields': (
            'waypoint_6_sensor',
            'waypoint_6_sensor_depth',
            'waypoint_6_sensor_message',
          )
      }),
      ('Waypoint 7 sensors', {
          'fields': (
            'waypoint_7_sensor',
            'waypoint_7_sensor_depth',
            'waypoint_7_sensor_message',
          )
      }),
      ('Waypoint 8 sensors', {
          'fields': (
            'waypoint_8_sensor',
            'waypoint_8_sensor_depth',
            'waypoint_8_sensor_message',
          )
      }),
      ('Waypoint 9 sensors', {
          'fields': (
            'waypoint_9_sensor',
            'waypoint_9_sensor_depth',
            'waypoint_9_sensor_message',
          )
      }),
      ('Waypoint 10 sensors', {
          'fields': (
            'waypoint_10_sensor',
            'waypoint_10_sensor_depth',
            'waypoint_10_sensor_message',
          )
      }),
      ('Order conf', {
          'fields': (
            'paid',
            'is_finished',
            'is_confirmed',
          )
      }),
      ('Order status', {
          'fields': (
            'status_1',
            'status_2',
            'status_3',
            'status_4',
            'status_5',
          )
      }),
    )

admin.site.register(Order, OrderAdmin)
