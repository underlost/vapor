from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    url(r'^admin42/', include(admin.site.urls)),
    url(r'^dota2/', include('vapor.dota2.urls', namespace='DOTA2')),
    url(r'^', include('vapor.core.urls', namespace='Core')),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
