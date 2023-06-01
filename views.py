from django.shortcuts import render
from .forms import OrderForm

PIZZA_SPIANATA = 12.50
PIZZA_SEPPI = 11.50
PIZZA_TIRATO = 10.50
OLIVES_PRICE = 2.50
CHEESE_PRICE = 1.50
DELIVERY_PRICE = 3.50

def order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            pizza_spianata = form.cleaned_data['pizza_spianata']
            pizza_seppi = form.cleaned_data['pizza_seppi']
            pizza_tirato = form.cleaned_data['pizza_tirato']
            extra_olives = form.cleaned_data['extra_olives']
            extra_cheese = form.cleaned_data['extra_cheese']
            delivery = form.cleaned_data['delivery']
            total_price = 0
            if extra_olives:
                total_price += OLIVES_PRICE
            if extra_cheese:
                total_price += CHEESE_PRICE
            if delivery:
                total_price += DELIVERY_PRICE
            if pizza_spianata:
                total_price += PIZZA_SPIANATA
            if pizza_seppi:
                total_price += PIZZA_SEPPI
            if pizza_tirato:
                total_price += PIZZA_TIRATO
            return render(request, 'order_confirmation.html', {'pizza_spianata': pizza_spianata, 'pizza_seppi': pizza_seppi, 'pizza_tirato': pizza_tirato,
                                   'extra_olives': extra_olives, 'extra_cheese': extra_cheese, 'delivery': delivery, 'total_price': total_price})
    else:
        form = OrderForm()
    return render(request, 'order.html', {'form': form, 'PIZZA_SPIANATA': PIZZA_SPIANATA,'PIZZA_SEPPI': PIZZA_SEPPI,'PIZZA_TIRATO': PIZZA_TIRATO,
                 'OLIVES_PRICE': OLIVES_PRICE, 'CHEESE_PRICE': CHEESE_PRICE, 'DELIVERY_PRICE': DELIVERY_PRICE})


