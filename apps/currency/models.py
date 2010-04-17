# -*- mode: python; coding: utf-8; -*- 
"""
models.py

Created by jbo on 2010-02-01.
Copyright (c) 2010 __MyCompanyName__. All rights reserved.
"""

#from l10n.utils import moneyfmt
from decimal import Decimal
from livesettings import config_value, SettingNotSet, config_value_safe, config_choice_values, config_get
from django.db import models
from l10n.models import Currencies
#from django.db.models import Q
#from currency.fields import CurrencyField
#from django.db.models.aggregates import Min
from django.utils.translation import ugettext_lazy as _
import logging

import config
#import datetime
#from decimal import Decimal

log = logging.getLogger('currency.models')

class CurrencyManager(models.Manager):
    def get_default(self):
        """Convenience method to get the default currency"""
        code, name = config_choice_values('CURRENCIES','CURRENCY_DEAULT')[0]
        try:
            return self.get(currency__iso3_code = code, active=True)
        except Currency.DoesNotExist:
            log.error('is not set default currency')
    
    def get_currency(self, code):
        """
        get the currency
        code - ISO alpha-3
        example: Currency.objects.get_currency("USD")
        """
        try:
            return self.get(currency__iso3_code = str(code).upper(), active=True)
        except Currency.DoesNotExist:
            log.error('is not set currency: %s' % str(code).upper())
    
    def currency_list(self):
        """
        Example
            return: [(u'USD', u'US Dollar'), (u'EUR', u'Euro')]
        """
        return self.values_list('currency__iso3_code', 'currency__name')
        
    def set_currency(self, rate, code='usd'):
        """"""
        cur_new = self.get_currency(code)
        if not isinstance(rate, Decimal):
            rate = Decimal(str(rate))
        cur_new.exchange_rate = rate
        cur_new.save()
        

    def from_request(self, request):
        """Get the current currency from the request"""
        currency = None
        if hasattr(request, 'session') and 'currency' in request.session:
            currencyid = request.session['currency']
            try:
                currency = Currency.objects.get(id=currencyid)
            except Currency.DoesNotExist:
                log.debug('Removing invalid currency from session')
                del request.session['currency']

        if not currency:
            currency = Currency.objects.get_default()

        #log.debug("Currency: %s", currency)
        return currency

class Currency(models.Model):
    """ A currency for using with a price
    """
    currency = models.ForeignKey(Currencies, verbose_name=_(u'Currency Name'))
    exchange_rate = models.DecimalField('Exchange rate', default="1.0", max_digits=18, decimal_places=4, 
                                       help_text=_("This rate is used to calculate the price from the base currency if a product has no price for this currency."))
    active = models.BooleanField(_('active'), default=True, help_text=_('The currency will be available.'))
    start_date = models.DateTimeField(_(u'Start Date'))
    
    objects = CurrencyManager()
    
    @property
    def country(self):
        """"""
        return ''
    
    @property
    def name(self):
        """"""
        return self.currency.name
    
    @property
    def code(self):
        """ISO alpha-3"""
        return self.currency.iso3_code
    #----------------------------------------------------------------------
    def numeric(self):
        """"""
        return self.currency.numcode
    
    def __unicode__(self):
        return self.code
    
    #def get_format_symbol(self):
    #    return self.symbol or self.code
    #format_symbol = property(get_format_symbol)

    #def format(self, val, places=-1, grouping=True, wrapcents='', current_locale=None):
    #    curr = self.format_symbol
    #    return moneyfmt(val, curr=curr, places=places, grouping=grouping, wrapcents=wrapcents, current_locale=current_locale)

    class Meta:
        #ordering = ('name', 'start_date',)
        verbose_name = _("Currency")
        verbose_name_plural = _("Currencies")


#import listeners
#listeners.start_default_listening()
