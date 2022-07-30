from django.db.models import (
    CharField,
    Model,
)


class Country(Model):
    country: CharField = CharField(max_length=2, primary_key=True)

    def __str__(self):
        return self.country

    class Meta:
        app_label: str = "news"
        verbose_name_plural: str = "countries"
