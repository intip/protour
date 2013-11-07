#-*- coding:utf-8 -*-

from django.conf.urls import patterns, url, include
from django.core.urlresolvers import reverse_lazy
from django.conf import settings
from django.views.generic import TemplateView


urlpatterns = patterns(
    'core.views',
    url(r'^$', 'homepage', name='homepage'),
    url(r'^pacote/$', TemplateView.as_view(template_name="pacote_details.html")),
)
