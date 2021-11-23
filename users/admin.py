from django.contrib import admin
from django.contrib.auth.models import Group

from users.models.subscription import Subscription

admin.site.register(Subscription)
admin.site.unregister(Group)
