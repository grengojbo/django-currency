===============
Django Currency
===============

**Django Currency** is a pluggable application for `Django Web Framework`_ and
`Satchmo`_ added support for multiple currencies.

.. _`Django Web Framework`: http://www.djangoproject.com 
.. _`Satchmo`: http://www.satchmoproject.com/

Installing & Setup
==================

Smuggler is in the `Python Package Index (PyPI)`_ and you can easily install
the latest stable version of it using the tools ``pip``. Try::

  pip install django-currency


Alternatively, you can install Smuggler from source code running the follow
command on directory that contains the file ``setup.py``::

  python setup.py install

After installation you need configure your project to recognizes the Currency
application adding ``'currency'`` to your ``INSTALLED_APPS`` setting and setup
the project::

  INSTALLED_APPS = (
    #...
    'keyedcache',
    'livesettings',
    'l10n',
    'south',
    'currency',
    #...
  )

Try::
  ./manage.py syncdb
  ./manage.py loaddata l10n_data
  ./manage.py loaddata currency_data

Settings
````````

Then try access these urls:

* `/settings/ <http://127.0.0.1:8000/settings/>`_, edit available currencies
  in section Currency Setting;

Currency Features
=====================

Current Features
----------------



