from django.conf.urls import include, url
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers
from retail import views
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic.base import TemplateView
admin.autodiscover()

import website.views

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', website.views.index, name='index'),
    url(r'^db', website.views.db, name='db'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^projects/', views.ProjectList.as_view()),
    url(r'^info/', views.AboutUs.as_view()),
    url(r'^contactinfo/', views.Contact.as_view()),
]

if settings.DEBUG is True:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



urlpatterns = format_suffix_patterns(urlpatterns)

