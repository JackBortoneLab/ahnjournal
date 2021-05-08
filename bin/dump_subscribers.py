#!/usr/bin/env python

from newsletter.models import Subscription

objects = Subscription.objects.all()

for item in objects:
    print(item.email)

