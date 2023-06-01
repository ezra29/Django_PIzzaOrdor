from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['pizza_spianata','pizza_seppi','pizza_tirato', 'extra_olives', 'extra_cheese', 'delivery']