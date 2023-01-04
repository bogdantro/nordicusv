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
          'fields': ('onetime', 'onetime_time', 'interval', 'date_start', 'date_end', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'choose_interval',)
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
      ('Waypoint 11 sensors', {
          'fields': (
            'waypoint_11_sensor',
            'waypoint_11_sensor_depth',
            'waypoint_11_sensor_message',
          )
      }),
      ('Waypoint 12 sensors', {
          'fields': (
            'waypoint_12_sensor',
            'waypoint_12_sensor_depth',
            'waypoint_12_sensor_message',
          )
      }),
      ('Waypoint 13 sensors', {
          'fields': (
            'waypoint_13_sensor',
            'waypoint_13_sensor_depth',
            'waypoint_13_sensor_message',
          )
      }),
      ('Waypoint 14 sensors', {
          'fields': (
            'waypoint_14_sensor',
            'waypoint_14_sensor_depth',
            'waypoint_14_sensor_message',
          )
      }),
      ('Waypoint 15 sensors', {
          'fields': (
            'waypoint_15_sensor',
            'waypoint_15_sensor_depth',
            'waypoint_15_sensor_message',
          )
      }),
      ('Waypoint 16 sensors', {
          'fields': (
            'waypoint_16_sensor',
            'waypoint_16_sensor_depth',
            'waypoint_16_sensor_message',
          )
      }),
      ('Waypoint 17 sensors', {
          'fields': (
            'waypoint_17_sensor',
            'waypoint_17_sensor_depth',
            'waypoint_17_sensor_message',
          )
      }),
      ('Waypoint 18 sensors', {
          'fields': (
            'waypoint_18_sensor',
            'waypoint_18_sensor_depth',
            'waypoint_18_sensor_message',
          )
      }),
      ('Waypoint 19 sensors', {
          'fields': (
            'waypoint_19_sensor',
            'waypoint_19_sensor_depth',
            'waypoint_19_sensor_message',
          )
      }),
      ('Waypoint 20 sensors', {
          'fields': (
            'waypoint_20_sensor',
            'waypoint_20_sensor_depth',
            'waypoint_20_sensor_message',
          )
      }),
      ('Waypoint 21 sensors', {
          'fields': (
            'waypoint_21_sensor',
            'waypoint_21_sensor_depth',
            'waypoint_21_sensor_message',
          )
      }),
      ('Waypoint 22 sensors', {
          'fields': (
            'waypoint_22_sensor',
            'waypoint_22_sensor_depth',
            'waypoint_22_sensor_message',
          )
      }),
      ('Waypoint 23 sensors', {
          'fields': (
            'waypoint_23_sensor',
            'waypoint_23_sensor_depth',
            'waypoint_23_sensor_message',
          )
      }),
      ('Waypoint 24 sensors', {
          'fields': (
            'waypoint_24_sensor',
            'waypoint_24_sensor_depth',
            'waypoint_24_sensor_message',
          )
      }),
      ('Waypoint 25 sensors', {
          'fields': (
            'waypoint_25_sensor',
            'waypoint_25_sensor_depth',
            'waypoint_25_sensor_message',
          )
      }),
      ('Waypoint 26 sensors', {
          'fields': (
            'waypoint_26_sensor',
            'waypoint_26_sensor_depth',
            'waypoint_26_sensor_message',
          )
      }),
      ('Waypoint 27 sensors', {
          'fields': (
            'waypoint_27_sensor',
            'waypoint_27_sensor_depth',
            'waypoint_27_sensor_message',
          )
      }),
      ('Waypoint 28 sensors', {
          'fields': (
            'waypoint_28_sensor',
            'waypoint_28_sensor_depth',
            'waypoint_28_sensor_message',
          )
      }),
      ('Waypoint 29 sensors', {
          'fields': (
            'waypoint_29_sensor',
            'waypoint_29_sensor_depth',
            'waypoint_29_sensor_message',
          )
      }),
      ('Waypoint 30 sensors', {
          'fields': (
            'waypoint_30_sensor',
            'waypoint_30_sensor_depth',
            'waypoint_30_sensor_message',
          )
      }),
      ('Waypoint 31 sensors', {
          'fields': (
            'waypoint_31_sensor',
            'waypoint_31_sensor_depth',
            'waypoint_31_sensor_message',
          )
      }),
      ('Waypoint 32 sensors', {
          'fields': (
            'waypoint_32_sensor',
            'waypoint_32_sensor_depth',
            'waypoint_32_sensor_message',
          )
      }),
      ('Waypoint 33 sensors', {
          'fields': (
            'waypoint_33_sensor',
            'waypoint_33_sensor_depth',
            'waypoint_33_sensor_message',
          )
      }),
      ('Waypoint 34 sensors', {
          'fields': (
            'waypoint_34_sensor',
            'waypoint_34_sensor_depth',
            'waypoint_34_sensor_message',
          )
      }),
      ('Waypoint 35 sensors', {
          'fields': (
            'waypoint_35_sensor',
            'waypoint_35_sensor_depth',
            'waypoint_35_sensor_message',
          )
      }),
      ('Waypoint 36 sensors', {
          'fields': (
            'waypoint_36_sensor',
            'waypoint_36_sensor_depth',
            'waypoint_36_sensor_message',
          )
      }),
      ('Waypoint 37 sensors', {
          'fields': (
            'waypoint_37_sensor',
            'waypoint_37_sensor_depth',
            'waypoint_37_sensor_message',
          )
      }),
      ('Waypoint 38 sensors', {
          'fields': (
            'waypoint_38_sensor',
            'waypoint_38_sensor_depth',
            'waypoint_38_sensor_message',
          )
      }),
      ('Waypoint 39 sensors', {
          'fields': (
            'waypoint_39_sensor',
            'waypoint_39_sensor_depth',
            'waypoint_39_sensor_message',
          )
      }),
      ('Waypoint 40 sensors', {
          'fields': (
            'waypoint_40_sensor',
            'waypoint_40_sensor_depth',
            'waypoint_40_sensor_message',
          )
      }),
    )

admin.site.register(Order, OrderAdmin)
