from django.conf.urls.defaults import patterns, include, url
from django.contrib.auth.views import login
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic.simple import direct_to_template

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', direct_to_template, dict(template='oreills/about.html.haml')),
    #url(r'^about/$', direct_to_template, dict(template='oreills/about.html.haml')),
    url(r'^contact/$', direct_to_template, dict(template='oreills/contact.html.haml')),
    url(r'^projects/$', direct_to_template, dict(template='oreills/projects.html.haml')),
    url(r'^projects/av$', direct_to_template, dict(template='av/av.html.haml')),
    # url(r'^oreills/', include('oreills.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    (r'^accounts/login/$', 'django.contrib.auth.views.login'),
    (r'^accounts/logout/$', 'django.contrib.auth.views.logout'),

    (r'^subterreader/', include('subterreader.urls')),
)

urlpatterns += staticfiles_urlpatterns()
