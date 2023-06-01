from django.db import models

class Order(models.Model):
    pizza_spianata = models.BooleanField(default=False)
    pizza_seppi = models.BooleanField(default=False)
    pizza_tirato = models.BooleanField(default=False)
    extra_olives = models.BooleanField(default=False)
    extra_cheese = models.BooleanField(default=False)
    delivery = models.BooleanField(default=False)
    total_price = models.DecimalField(max_digits=6, decimal_places=2)
    date_ordered = models.DateTimeField(auto_now_add=True)
