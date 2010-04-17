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
the latest stable version of it using the tools ``pip`` or
``easy_install``. Try::

  pip install django-currency

or::

  easy_install django-currency

.. _`Python Package Index (PyPI)`: http://pypi.python.org 


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

Currency support.

    - All display items are driven by templates using the powerful Django templating language
    - All urls can be custom configured to your desired naming convention
    - The checkout process can be tailored to your specific needs


Signals in Currency
===================

Signals are a very powerful tool available in Django that allows you to decouple aspects of your application. The `Django Signals Documentation`_, has this summary:
   
    "In a nutshell, signals allow certain senders to notify a set of receivers that some action has taken place."

In addition to all of the built in `Django signals`_, Currency includes a number of store related signals. By using these signals, you can add very unique customizations to your store without needing to modify the Satchmo code.

Signal Descriptions
--------------------

livesettings.signals
^^^^^^^^^^^^^^^^^^^^

configuration_value_changed
***************************

Sent after a value from the configuration application has been changed.

Arguments sent with this signal:

    ``sender``
        The instance of ``livesettings.values.Value`` that was changed
        
    ``old_value``
        The old value of the setting
        
    ``new_value``
        The new value of the settings
        
    ``setting``
        The instance of ``livesettings.values.Value`` that was changed (Note: this argument is the same as ``sender``)


satchmo_cart_changed
********************

Sent whenever the status of the cart has changed. For example, when an item is added, removed, or had it's quantity updated.

Arguments sent with this signal:

    ``sender``
        The instance of ``satchmo_store.shop.models.Cart`` that was changed

    ``cart``
        The instance of ``satchmo_store.shop.models.Cart`` that was changed (Note: this argument is the same as ``sender``)

    ``request``
        The ``HttpRequest`` object used in the view to change the cart

  .. _Django Signals Documentation: http://docs.djangoproject.com/en/dev/topics/signals/
  .. _Django signals: http://docs.djangoproject.com/en/dev/ref/signals/
  
Test
====

To install the latest stable version::

	pip install git+git://github.com/dcramer/django-devserver#egg=django-devserver


django-devserver has some optional dependancies, which we highly recommend installing.

* ``pip install sqlparse`` -- pretty SQL formatting
* ``pip install werkzeug`` -- interactive debugger
* ``pip install guppy`` -- tracks memory usage (required for MemoryUseModule)

You will need to include ``devserver`` in your ``INSTALLED_APPS``::

	INSTALLED_APPS = (
	    'devserver',
	    ...
	)

Specify modules to load via the ``DEVSERVER_MODULES`` setting::

	DEVSERVER_MODULES = (
	    'devserver.modules.sql.SQLRealTimeModule',
	    'devserver.modules.sql.SQLSummaryModule',
	    'devserver.modules.profile.ProfileSummaryModule',

	    # Modules not enabled by default
	    #'devserver.modules.profile.MemoryUseModule',
	    #'devserver.modules.cache.CacheSummaryModule',
	)

Disable SQL query truncation (used in SQLRealTimeModule) with the ``DEVSERVER_TRUNCATE_SQL`` setting::

	DEVSERVER_TRUNCATE_SQL = False

