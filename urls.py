from django.conf.urls.defaults import patterns, include, url
from django.contrib.auth.views import login
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'oreills.views.home', name='home'),
    # url(r'^oreills/', include('oreills.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    (r'^accounts/login/$', 'django.contrib.auth.views.login'),

    (r'^subterreader/$', 'subterreader.views.manage'),
    (r'^subterreader/read/$', 'subterreader.views.read'),
    (r'^subterreader/settings/$', 'subterreader.views.settings'),
    (r'^subterreader/iframe/(?P<url>.+)$', 'subterreader.views.iframe'),
)

urlpatterns += staticfiles_urlpatterns()
