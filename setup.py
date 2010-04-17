# -*- mode: python; coding: utf-8; -*- 
import ez_setup
ez_setup.use_setuptools()
from setuptools import setup, find_packages
import os, os.path
import sys

DIRNAME = os.path.dirname(__file__)

# Dynamically calculate the version based on django.VERSION.
version = __import__('currency').__version__
packages = find_packages('satchmo/apps')
packages.append('docs')

setup(name='django-currency',
    version=version,
    description="Multiple currencies",
    long_description="Added support for multiple currencies as Satchmo and Django applications",
    keywords='satchmo',
    author='Oleg Dolya',
    author_email='oleg.dolya@gmail.com',
    url='http://bitbucket.org/jbo/django-currency/',
    license='GPL',
    include_package_data=True,
    package_dir = {
      '' : 'apps',
      'docs' : 'docs',
      },
    #scripts=['scripts/'],
    setup_requires=["setuptools_hg"],
    #data_files = data_files,
    zip_safe = False,
    # install_requires=[
    #     'Django>=1.1',
    #     'django-extensions',
    #     'BeautifulSoup',
    #     #'userprofile',
    # ],
    packages = packages,
    classifiers=['Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities'],
)
