from django.urls import path
from .views import *

urlpatterns = [

    path('', index , name='base'),
    path('product_details/<pk>', product_details,name='product-details'),
    path('contact', contact, name='contact-us'),
    path('about', aboutus , name='About'),
    path('search', product_search , name='product-search'),

   
]