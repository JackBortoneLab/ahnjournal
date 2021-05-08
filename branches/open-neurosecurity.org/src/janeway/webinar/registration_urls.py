from django.conf.urls import url

from newsletter_subscription.ajax_views import ajax_subscribe
from .views import form, subscribe, resubscribe


def webinar_subscriptions_urlpatterns(**kwargs):
    return [
        url(
            r'^(?P<slug>[\w]+)/$',
            form,
            kwargs,
            name='webinar_subscription_form',
        ),
        url(
            r'^s/(?P<code>[^/]+)/$',
            subscribe,
            kwargs,
            name='webinar_subscription_subscribe',
        ),
        url(
            r'^r/(?P<code>[^/]+)/$',
            resubscribe,
            kwargs,
            name='webinar_subscription_resubscribe',
        ),

        url(
            r'^ajax_subscribe/$',
            ajax_subscribe,
            kwargs,
            name='webinar_subscription_ajax_subscribe',
        ),
    ]
