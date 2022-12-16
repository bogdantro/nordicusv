from django.contrib import admin
from .models import *


class OrderAdmin(admin.ModelAdmin):
    list_filter  = ['user']
    list_display =['id', 'name', 'user', 'created_at', 'paid']

admin.site.register(Order, OrderAdmin)
