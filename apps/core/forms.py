from django.db.models import fields
from django import forms
from .models import Order

class Order(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(Order, self).__init__(*args, **kwargs)

    class Meta:
        model = Order
        fields = ('name', 'email', 'message', 'route_cords', 'time', 'custom_cords', 'user_html', 'sensor_1_waypoins', 'sensor_1_depth')
