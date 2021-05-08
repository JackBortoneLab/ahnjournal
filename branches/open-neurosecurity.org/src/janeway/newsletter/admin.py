from django.contrib import admin
from .models import Subscription


class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email')


admin_list = [
    (Subscription, SubscriptionAdmin),
    ]

[admin.site.register(*t) for t in admin_list]
