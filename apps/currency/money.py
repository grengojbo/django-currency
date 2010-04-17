# -*- coding: utf-8 -*-
import exceptions
from decimal import Decimal
from currency.models import Currency

def set_default_currency(code=None):
    """
    setting default currency
    """
    global DEFAULT_CURRENCY
    if not code:
        DEFAULT_CURRENCY = Currency.objects.get_default()
    else:
        # TODO: to make currency to config
        pass

class IncorrectMoneyInputError(exceptions.Exception):
    def __init__(self):
        return
    def __str__(self):
        return "Incorrectly formatted monetary input!"

class Money:
    def __init__ (self, amount=Decimal("0.0"), currency=None):
        set_default_currency()
        if not isinstance(amount, Decimal):
            amount = Decimal(str(amount))
        self.amount = amount
        if not currency:
            self.currency = Currency.objects.get_default()
        else:
            if not isinstance(currency, Currency):
                currency = Currency.objects.get_currency(currency)
            self.currency = currency
    def __repr__(self):
        return '%s %5.2f' % (self.currency, self.amount)
    def __pos__(self):
        return Money(amount=self.amount, currency=self.currency)
    def __neg__(self):
        return Money(amount=-self.amount, currency=self.currency)
    def __add__(self, other):
        if isinstance(other, Money):
            if self.currency == other.currency:
                return Money(amount = self.amount + other.amount, currency = self.currency)
            else: 
                s = self.convert_to_default()
                other = other.convert_to_default()
                return Money(amount = s.amount + other.amount, currency = DEFAULT_CURRENCY)
        else:
            return Money(amount = self.amount + Decimal(str(other)), currency = self.currency)
    def __sub__(self, other):
        if isinstance(other, Money):
            if self.currency == other.currency:
                return Money(amount = self.amount - other.amount, currency = self.currency)
            else: 
                s = self.convert_to_default()
                other = other.convert_to_default()
                return Money(amount = s.amount - other.amount, currency = DEFAULT_CURRENCY)
        else:
            return Money(amount = self.amount - Decimal(str(other)), currency = self.currency)
    def __mul__(self, other):
        if isinstance(other, Money):
            raise TypeError, 'can not multiply monetary quantities'
        else:
            return Money(amount = self.amount*Decimal(str(other)), currency = self.currency)
    def __div__(self, other):
        if isinstance(other, Money):
            assert self.currency == other.currency, 'currency mismatch'
            return self.amount / other.amount
        else:
            return self.amount / Decimal(str(other))
    def __rmod__(self, other):
        """
        Calculate percentage of an amount.  The left-hand side of the operator must be a numeric value.  E.g.:
        >>> money = Money.Money(200, "USD")
        >>> 5 % money
        USD 10.00
        """
        if isinstance(other, Money):
            raise TypeError, 'invalid monetary operation'
        else:
            return Money(amount = Decimal(str(other)) * self.amount / 100, currency = self.currency)
    def convert_to_default(self):
        return Money(amount = self.amount * self.currency.exchange_rate, currency=DEFAULT_CURRENCY)
    def convert_to(self, currency):
        """
        Convert from one currency to another.
        """
        return None # TODO  (How??)

    __radd__ = __add__
    __rsub__ = __sub__
    __rmul__ = __mul__
    __rdiv__ = __div__

    #
    # Override comparison operators
    #
    def __eq__(self, other):
        if isinstance(other, Money):
            return (self.amount == other.amount) and (self.currency == other.currency)
        return (self.amount == Decimal(str(other)))
    def __ne__(self, other):
        result = self.__eq__(other)
        if result is NotImplemented:
            return result
        return not result
    def __lt__(self, other):
        if isinstance(other, Money):
            if (self.currency == other.currency):
                return (self.amount < other.amount)
            else:
                raise TypeError, 'can not compare different currencies'
        else:
            return (self.amount < Decimal(str(other)))
    def __gt__(self, other):
        if isinstance(other, Money):
            if (self.currency == other.currency):
                return (self.amount > other.amount)
            else:
                raise TypeError, 'can not compare different currencies'
        else:
            return (self.amount > Decimal(str(other)))
    def __le__(self, other):
        return self < other or self == other
    def __ge__(self, other):
        return self > other or self == other

    #
    # Miscellaneous helper methods
    #

    def allocate(self, ratios):
        """
        Allocates a sum of money to several accounts.
        """
        total = sum(ratios)
        remainder = self.amount
        results = []
        for i in range(0, len(ratios)):
            results.append(Money(amount = self.amount * ratios[i] / total, currency = self.currency))
            remainder -= results[i].amount
        i = 0
        while i < remainder:
            results[i].amount += Decimal("0.01")
            i += 1
        return results

    def spell_out(self):
        """
        Spells out a monetary amount.  E.g. "Two-hundred and twenty-six dollars and seventeen cents."
        """
        pass # TODO

    def from_string(self, s):
        """
        Parses a properly formatted string and extracts the monetary value and currency
        """
        try:
            self.amount = Decimal(str(s).strip())
            self.currency = DEFAULT_CURRENCY
        except:
            try:
                s = s.strip()
                self.currency = Currency.objects.get_currency(s[:3])
                self.amount = Decimal(s[3:].strip())
            except:
                raise IncorrectMoneyInputError
            
    def set_currency(self, amount, code='usd'):
        """"""
        if not isinstance(amount, Decimal):
            amount = Decimal(str(amount))
        #self.amount = amount
        Currency.objects.set_currency(amount, code)


