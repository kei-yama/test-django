# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http.response import HttpResponse
from .forms import ContactForm 


def index_template(request):
    # index_data = {'app': 'demo', 'is_weekday': True}
    # return render(request, 'index.html', index_data)
    form = ContactForm()
    return render(request, 'index.html', {
        'form': form,
    })
