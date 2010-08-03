from django.conf.urls.defaults import *
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^', include('main.urls')),
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),

    # auth
    url(r'^info/?$', 'auth.views.info', name='auth_info'),
    url(r'^login/?$', 'auth.views.login', name='auth_login'),
    url(r'^login/callback/?$', 'auth.views.callback', name='auth_callback'),
    url(r'^logout/?$', 'auth.views.logout', name='auth_logout'),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT
        }),
    )

