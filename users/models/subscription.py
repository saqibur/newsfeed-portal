from django.conf import settings
from django.db.models import (
    ManyToManyField,
    Model,
    OneToOneField,
    CASCADE,
)

from news.models.country import Country
from news.models.keyword import Keyword
from news.models.source import Source


class Subscription(Model):
    user: OneToOneField = OneToOneField(
        to=settings.AUTH_USER_MODEL,
        unique=True,
        on_delete=CASCADE,
    )

    countries: ManyToManyField = ManyToManyField(Country, related_name="countries")
    sources: ManyToManyField = ManyToManyField(Source, related_name="sources")
    keywords: ManyToManyField = ManyToManyField(Keyword, related_name="keywords")

    def __str__(self):
        return str(self.user)
