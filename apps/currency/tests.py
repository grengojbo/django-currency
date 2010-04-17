# -*- mode: python; coding: utf-8; -*-

# Author:  oleg --<oleg.dolya@gmail.com>
# Purpose: 
# Created: 05.02.2010

"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""

import unittest
from django import test
from django.test.client import Client
from models import Currency
from decimal import Decimal
from money import Money
import logging

__author__ = '$Author:$'
__revision__ = '$Revision:$'

l = logging.getLogger('moodname.tests') 

class CurrencyTestCase(test.TestCase):
    fixtures = ['test_currency']
    def setUp(self):
        # Every test needs a client.
        self.client = Client()
        
    def testCurrency(self):
        cur = Currency.objects.get_default()
        self.assertEquals("USD", cur.code)
        exc = Currency.objects.get_currency("EUR")
        self.assertEquals(Decimal('1.39'), exc.exchange_rate)
        exc.exchange_rate = Decimal('1.5')
        exc.save()
        exc2 = Currency.objects.get_currency("EUR")
        self.assertEquals(Decimal('1.5'), exc2.exchange_rate)
        self.assertNotEqual(Decimal('8.11'), exc2.exchange_rate)
        
        #exc3 = Currency.objects.get_currency("UAH")
        #self.assertNotEqual(Decimal('8.11'), exc3.exchange_rate)
        
    def testMoney(self):
        """"""
        USD100 = Money(100, "USD")
        EUR100 = Money(100, "EUR")
        self.assertEquals(Decimal(139),EUR100.convert_to_default())
        self.assertEquals(Decimal(100),EUR100.convert_to_default() - 39)
        Currency.objects.set_currency('1.5', 'EUR')
        exc2 = Currency.objects.get_currency("EUR")
        self.assertEquals(Decimal('1.5'), exc2.exchange_rate)
        EUR1000 = Money(1000, "EUR")
        self.assertEquals(Decimal(1500),EUR1000.convert_to_default())
        self.assertNotEquals(Decimal(150),EUR100.convert_to_default())
        #EUR100.set_currency('1.6', 'EUR')
        #self.assertEquals(Decimal(160),EUR100.convert_to_default())
        #exc3 = Currency.objects.get_currency("EUR")
        #self.assertEquals(Decimal('1.6'), exc3.exchange_rate)
