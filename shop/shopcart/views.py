from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shopshop.models import *
from .cart import *
from .forms import *

@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(ProductList, id=product_id)
    form = CartAddForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product = product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart:cart_detail')

def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(ProductList, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')
def cart_detail(request):
    cart = Cart(request)
    return render(request, 'shopcart/detail.html', {'cart': cart})

