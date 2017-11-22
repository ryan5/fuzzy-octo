# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=25) #Any Characters
    description = models.TextField(default="", blank=True)
    price = models.DecimalField(max_digits=100, decimal_places=2, default=0.00, blank=True) #100.00
    sales_price = models.DecimalField(max_digits=100, decimal_places=2, default=0.00, blank=True)
    
    def __unicode__(self):
        return self.title