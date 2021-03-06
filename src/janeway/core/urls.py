from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
from django.conf import settings
from django.views.static import serve

from janeway.press import views as press_views

include('events.registration')

urlpatterns = [
    url(r'^$', press_views.index, name='website_index'),
    url(r'^summernote/', include('django_summernote.urls')),
    url(r'', include('core.include_urls')),
    url(r'^404/$', TemplateView.as_view(template_name='404.html')),
    url(r'^500/$', TemplateView.as_view(template_name='500.html'))
    ]
