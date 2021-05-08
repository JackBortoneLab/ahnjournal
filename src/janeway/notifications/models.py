from django.db import models
from django.utils import timezone
from django.db.models import Q
from datetime import timedelta

from cron import logic
from journal import models as journal_models
from utils import render_template, notify_helpers

class Notification(models.Model):
    user = models.ForeignKey('core.Author', blank=False, null=False)
    message = models.CharField(max_length=255)
    notification_type = 'reminder' 

    def url(self):
        """/ahnjournal/i/notifications/<id>/"""
        pass

