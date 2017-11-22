# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ["__unicode__","title","description","price","sales_price"]
    search_fields = ["description"]
    list_editable = ["sales_price"]
    class Meta:
        model = Product
    
    
admin.site.register(Product, ProductAdmin)