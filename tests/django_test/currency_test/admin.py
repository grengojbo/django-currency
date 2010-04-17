# -*- mode: python; coding: utf-8; -*- 
"""
admin.py

Created by jbo on 2010-02-01.
Copyright (c) 2010 __MyCompanyName__. All rights reserved.
"""
from currency_test.models import Entity, Entity_0_USD, Entity_USD
from django.contrib import admin 
from django.utils.translation import ugettext_lazy as _


admin.site.register(Entity)
admin.site.register(Entity_0_USD)
admin.site.register(Entity_USD)
