from django.conf.urls.defaults import *
from os.path import join, dirname
from django.conf import settings
from django.contrib import admin

admin.autodiscover()
urlpatterns = getattr(settings, 'URLS', [])
adminpatterns = patterns('',
                         (r'^admin/doc/', include('django.contrib.admindocs.urls')),
                         (r'^admin/', include(admin.site.urls)),
)
sitepattern =  patterns('',
                        #(r'^accounts/', include('satchmo_store.accounts.urls')),
                        url(r'^jsi18n/(?P<packages>\S+?)/$', 'django.views.i18n.javascript_catalog', name="i18n-js"),
                        (r'^settings/', include('livesettings.urls')),
                        (r'^cache/', include('keyedcache.urls')),
                        (r'^i18n/', include('l10n.urls')),
)
if urlpatterns:
    urlpatterns += adminpatterns + sitepattern
else:
    urlpatterns = adminpatterns + sitepattern

##urlpatterns += patterns('django_test.views',
##    ('^regular_form/$', 'regular_form'),
##    ('^regular_form/(?P<id>\d+)/$', 'regular_form_edit'),
##    ('^model_form/$', 'model_form'),
##    ('^model_form/(?P<id>\d+)/$', 'model_form_edit'),
##    
##)

urlpatterns += patterns('',
                        ('^$', 'django.views.generic.simple.redirect_to', {'url': '/admin/'}),
#    #url(r'^admin-media/(.*)$', 'django.views.static.serve', {'document_root': join(dirname(admin.__file__), 'media')}),
#    url(r'^admin-media/(.*)$', 'django.views.static.serve', {'document_root': join(dirname(grappelli.__path__[0]), 'grappelli/media')}),
#    url(r'^grappelli/', include('grappelli.urls')),
)