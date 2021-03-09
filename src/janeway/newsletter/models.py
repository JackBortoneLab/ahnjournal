from django.db import models
from django.utils import timezone
from django.db.models import Q
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.contenttypes.models import ContentType
from django.utils.translation import ugettext_lazy as _

#from newsletter_subscription.models import SubscriptionBase

class Subscription(models.Model):
    full_name = models.CharField("Full name", max_length=100, blank=True)
    email = models.EmailField(_('email address'), max_length=254, unique=True)
    is_active = models.BooleanField(_('is active'), default=True)

    class Meta:
        app_label = 'newsletter'
        abstract = False
        db_table = 'newsletter_subscription'

    def __str__(self):
        return self.email    
