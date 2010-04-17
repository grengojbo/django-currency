# -*- mode: python; coding: utf-8; -*- 
"""
admin.py

Created by jbo on 2010-02-01.
Copyright (c) 2010 __MyCompanyName__. All rights reserved.
"""
from currency.models import Currency
from django.contrib import admin 
from django.utils.translation import ugettext_lazy as _

class CurrencyOptions(admin.ModelAdmin):
    list_display=('name', 'exchange_rate', 'start_date',)
    ordering = ['currency', '-start_date']
    save_as = True
    save_on_top = True

admin.site.register(Currency, CurrencyOptions)
