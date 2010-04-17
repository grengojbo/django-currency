# -*- mode: python; coding: utf-8; -*- 

# Author:  Oleg --<oleg.dolya@gmail.com>
# Purpose: 
# Created: 03.02.2010

from django.utils.translation import ugettext_lazy as _
from livesettings import config_register, ConfigurationGroup, StringValue
#from currency.money import Money
from l10n.models import Currencies
import logging


log = logging.getLogger('currency.config')

CURRENCY_GROUP = ConfigurationGroup('CURRENCIES',_('Currency Setting'))

CURRENCY_DEAULT = config_register(StringValue(CURRENCY_GROUP,
    'CURRENCY_DEAULT',
    #requires = CURRENCY_AVAILABLE,
    description=_("Default Currency"),
    help_text=_("Select default currency value."),
    default="USD",
    #choices=CURRENCY_AVAILABLE
    choices=[(code, name) for code, name in Currencies.objects.currency_list()]
    ))  

#def active_currency():
#    active_currencies = config_choice_values('CURRENCIES', 'CURRENCY_AVAILABLE')
#    log.debug('--------------------------')
#    c =config_get(CURRENCY_GROUP,'CURRENCY_AVAILABLE')
#    log.debug(c.value)
#    log.debug(config_value('LANGUAGE', 'SHOW_TRANSLATIONS'))