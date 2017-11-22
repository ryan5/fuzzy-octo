# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def detail_view(request):
    print request
    template = "detail_view.html"
    context = {
        "title":"Detailed View"
    }
    return render(request, template, context)

def list_view(request):
    print request
    template = "list_view.html"
    context = {
        "title":"Listed View"
    }
    return render(request, template, context)