from django.urls import path
from .views import *

urlpatterns = [
    path('', Shop.as_view(), name='shop'),
    path('categories/', show_categories, name='categories'),
    path('shop-single/', show_single, name='single')

]
