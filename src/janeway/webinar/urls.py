from django.conf.urls import url, include

from .models import Subscription
from .backend import ModelBackend
from .registration_urls import webinar_subscriptions_urlpatterns

urlpatterns = [
        url(r'', include(webinar_subscriptions_urlpatterns(
            backend=ModelBackend(Subscription)))
            )
]
