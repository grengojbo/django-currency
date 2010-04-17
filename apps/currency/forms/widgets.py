from django import forms
from currency.money import Money
from currency.models import Currency
from decimal import Decimal

__all__ = ('InputMoneyWidget', 'CurrencySelect',)

#CURRENCY_CHOICES = ((c.code, c.name) for i, c in CURRENCY.items() if c.code != 'XXX')

class CurrencySelect(forms.Select):
    #def __init__(self, attrs=None, choices=((code, name) for code, name in Currency.objects.currency_list())):
    def __init__(self, attrs=None, choices=Currency.objects.currency_list()):
        super(CurrencySelect, self).__init__(attrs, choices)
    
class InputMoneyWidget(forms.TextInput):
    
    def __init__(self, attrs=None, currency_widget=None):
        self.currency_widget = currency_widget
        if not self.currency_widget:
            self.currency_widget = CurrencySelect()
        super(InputMoneyWidget, self).__init__(attrs)
    
    def render(self, name, value, attrs=None):
        amount = ''
        currency = ''
        if isinstance(value, Money):
            amount = value.amount
            currency = value.currency.code
        if isinstance(value, tuple):
            amount = value[0]
            currency = value[1]
        if isinstance(value, int) or isinstance(value, Decimal):
            amount = value
        result = super(InputMoneyWidget, self).render(name, amount)
        result += self.currency_widget.render(name+'_currency', currency)
        return result
    
    def value_from_datadict(self, data, files, name):
        return (data.get(name, None), data.get(name+'_currency', None))

##from decimal import Decimal
##from django import forms
##from django.utils.safestring import mark_safe
##from django.utils.translation import ugettext_lazy as _
##from livesettings import config_value
##from satchmo_utils.numbers import round_decimal
##import logging
##
##log = logging.getLogger('satchmo_utils.widgets')
##
##def _render_decimal(value, places=2, min_places=2):
##
##    if value is not None:
##        roundfactor = "0." + "0"*(places-1) + "1"
##        if value < 0:
##            roundfactor = "-" + roundfactor
##        
##        value = round_decimal(val=value, places=places, roundfactor=roundfactor, normalize=True)
##        log.debug('value: %s' % type(value))
##        parts = ("%f" % value).split('.')
##        n = parts[0]
##        d = ""
##    
##        if len(parts) > 0:
##            d = parts[1]
##        elif min_places:
##            d = "0" * min_places
##        
##        while len(d) < min_places:
##            d = "%s0" % d
##        
##        while len(d) > min_places and d[-1] == '0':
##            d = d[:-1]
##    
##        if len(d) > 0:
##            value = "%s.%s" % (n, d)
##        else:
##            value = n
##    return value
##
##class BaseCurrencyWidget(forms.TextInput):
##    """
##    A Text Input widget that shows the currency amount
##    """
##    def __init__(self, attrs={}):
##        final_attrs = {'class': 'vCurrencyField'}
##        if attrs is not None:
##            final_attrs.update(attrs)
##        super(BaseCurrencyWidget, self).__init__(attrs=final_attrs)
##
##    def with_currency(self, content):
##        """
##        Prepend a currency to the provided content if and only if this is a single currency store.
##        """
##        from satchmo_store.shop.models import Config
##        config = Config.objects.get_current()
##        if config.is_multi_currency:
##            # multi-currency store
##            return content
##        else:
##            # single-currency store
##            return mark_safe('<span class="currency">%s</span>%s' % (config.currency.format_symbol, content))
##        
##        
##class CurrencyWidget(BaseCurrencyWidget):
##    
##    def render(self, name, value, attrs=None):
##        if value != '':
##            value = _render_decimal(value, places=8)
##        rendered = super(CurrencyWidget, self).render(name, value, attrs)
##        return self.with_currency(rendered)
##        
##class TruncatedCurrencyWidget(BaseCurrencyWidget):
##    """
##    A Text Input widget that shows the currency amount - stripped to two digits by default.
##    """
##                
##    def render(self, name, value, attrs=None):
##        value = _render_decimal(value, places=2)
##        rendered = super(TruncatedCurrencyWidget, self).render(name, value, attrs)
##        return self.with_currency(rendered)
##        
##class StrippedDecimalWidget(forms.TextInput):
##    """
##    A textinput widget that strips out the trailing zeroes.
##    """
##
##    def __init__(self, attrs={}):
##        final_attrs = {'class': 'vDecimalField'}
##        if attrs is not None:
##            final_attrs.update(attrs)
##        super(StrippedDecimalWidget, self).__init__(attrs=final_attrs)
##
##    def render(self, name, value, attrs=None):
##        value = _render_decimal(value, places=8, min_places=0)
##        return super(StrippedDecimalWidget, self).render(name, value, attrs)