from django.utils.translation import ugettext_lazy as _
from django import forms
from widgets import InputMoneyWidget
from currency.money import Money
from currency.models import Currency

__all__ = ('MoneyField',)

class MoneyField(forms.DecimalField):
    
    def __init__(self, currency_widget=None, *args, **kwargs):
        self.widget = InputMoneyWidget(currency_widget=currency_widget)
        super(MoneyField, self).__init__(*args, **kwargs)
    
    def clean(self, value):
        if not isinstance(value, tuple):
            raise Exception("Invalid value provided for MoneyField.clean (expected tupple)")
        amount = super(MoneyField, self).clean(value[0])
        currency = Currency.objects.get_currency(value[1])
        if not currency:
            raise forms.ValidationError(_(u'Input currency'))
        return Money(amount=amount, currency=currency)