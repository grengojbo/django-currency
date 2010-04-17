#!/usr/bin/env python
# encoding: utf-8
"""
fabfile.py

Created by jbo on 2009-12-11.
Copyright (c) 2009 __MyCompanyName__. All rights reserved.
"""

from __future__ import with_statement
from fabric.api import *
from fabric.contrib.console import confirm

def dist():
    """docstring for fsadist"""
    with cd('~/src/django-currency/tests/django_test/'):
        with settings(warn_only=True):
            result = local('./manage.py test currency', capture=False)
        if result.failed and not confirm("Tests failed. Continue anyway?"):
            abort("Aborting at user request.")
##        with settings(warn_only=True):
##            result = local('hg push', capture=False)
##        if result.failed and not confirm("Tests failed. Continue anyway?"):
##            abort("Aborting at user request.")    