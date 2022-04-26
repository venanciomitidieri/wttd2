"""eventex URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""

from django.contrib import admin
from django.urls import path
import eventex.core.views
import eventex.subscriptions.views
# from eventex.subscriptions.views import subscribe

urlpatterns = [
    path('',eventex.core.views.home),
    path('inscricao/',eventex.subscriptions.views.subscribe),
    path('admin/', admin.site.urls),
    
]










'''
from django.conf.urls import include, url
from django.contrib import admin
from eventex.core.views import home

from eventex.subscriptions.views import subscribe


urlpatterns = [
    url(r'^$', home),
    url('inscricao/', subscribe),
    url(r'^admin/', admin.site.urls),
]
'''