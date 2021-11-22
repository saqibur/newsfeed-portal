from django.db.models import (
    CharField,
    Model,
)



class Country(Model):
    country: CharField = CharField(max_length=100, primary_key=True)



    class Meta:
        app_label: str = 'news'
        verbose_name_plural: str = "countries"
