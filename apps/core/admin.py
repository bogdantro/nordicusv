from django.contrib import admin
from .models import *




class OrderAdmin(admin.ModelAdmin):
    list_filter  = ['user']
    list_display =['id', 'name', 'user', 'created_at', 'paid']
    readonly_fields = ['created_at']
    fieldsets = (
      ('User info', {
          'fields': ('user', 'user_html', 'name', 'email',)
      }),
      ('Survey info', {
          'fields': ('price', 'message',)
      }),
      ('Order conf', {
          'fields': (
            'paid',
            'is_finished',
            'is_confirmed',
            'created_at',
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
      ('Route cordinates', {
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
            'custom_cords_11',
            'custom_cords_12',
            'custom_cords_13',
            'custom_cords_14',
            'custom_cords_15',
            'custom_cords_16',
            'custom_cords_17',
            'custom_cords_18',
            'custom_cords_19',
            'custom_cords_20',
            'custom_cords_21',
            'custom_cords_22',
            'custom_cords_23',
            'custom_cords_24',
            'custom_cords_25',
            'custom_cords_26',
            'custom_cords_27',
            'custom_cords_28',
            'custom_cords_29',
            'custom_cords_30',
            'custom_cords_31',
            'custom_cords_32',
            'custom_cords_33',
            'custom_cords_34',
            'custom_cords_35',
            'custom_cords_36',
            'custom_cords_37',
            'custom_cords_38',
            'custom_cords_39',
            'custom_cords_40',
          )
      }),
      ('Time', {
          'fields': ('onetime', 'interval', 'onetime_time', 'interval_time',)
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
    )

admin.site.register(Order, OrderAdmin)
