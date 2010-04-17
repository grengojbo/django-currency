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

##CURRENCY_AVAILABLE = config_register(
##    BooleanValue(CURRENCY_GROUP,
##    'CURRENCY_METOD',
##    #requires = LANGUAGE_ALLOW_TRANSLATIONS,
##    description = _("Currency metod exchange"),
##    help_text=_("is default USD=1 Normal -EURO/USD=1.3984 Inverse - USD/EURO=0.719"),
##    #choices=[('','')]
##    choices=currency_choices()
##    ))

CURRENCY_DEAULT = config_register(StringValue(CURRENCY_GROUP,
    'CURRENCY_DEAULT',
    #requires = CURRENCY_AVAILABLE,
    description=_("Account Verification"),
    help_text=_("Select the style of account verification. 'Immediate' means no verification needed."),
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