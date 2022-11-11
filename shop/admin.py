from django import urls
from django.contrib import admin
from django.urls import path
from django.shortcuts import render


# Register your models here.
from .models import Product, Orders,Contact,OrderUpdate




admin.site.register(Product)
admin.site.register(OrderUpdate)

admin.site.register(Contact)
admin.site.register(Orders)