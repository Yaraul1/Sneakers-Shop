from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import *
from shopcart.forms import CartAddForm

def show_categories(request):
    category = Category.objects.all()
    page = 'category'
    context = {'category': category, 'page': page}
    return render(request, 'shopshop/_categories.html', context)


def show_single(request):
    return render(request, 'shopshop/shop-single.html')


def product_detail(request, id, slug):
    product = get_object_or_404(ProductList,
                                id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddForm()
    return render(request, 'shop/product/detail.html', {'product': product,
                                                        'cart_product_form': cart_product_form})

class Shop(ListView):
    model = ProductList
    template_name = 'shopshop/shop.html'
    context_object_name = 'products'
    paginate_by = 4

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

