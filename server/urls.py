"""drf_sample URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers
from retail import views
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic.base import TemplateView
admin.autodiscover()


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^projects/', views.ProjectList.as_view()),
    url(r'^info/', views.AboutUs.as_view()),
    url(r'^contactinfo/', views.Contact.as_view()),
    url(r'', include('retail.urls')),
]

if settings.DEBUG is True:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



urlpatterns = format_suffix_patterns(urlpatterns)