from django.conf.urls import url, include

from .models import Subscription
from newsletter_subscription.backend import ModelBackend
from newsletter_subscription.urls import newsletter_subscriptions_urlpatterns

urlpatterns = [
        url(r'', include(newsletter_subscriptions_urlpatterns(
            backend=ModelBackend(Subscription)))
            )
]
