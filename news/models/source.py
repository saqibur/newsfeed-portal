from django.db.models import (
    CharField,
    ForeignKey,
    Model,
    SET_NULL,
)

from news.models.country import Country



class Source(Model):
    source: CharField = CharField(max_length=100, primary_key=True)

    country: CharField = ForeignKey(
        to        = Country,
        blank     = True,
        null      = True,
        on_delete = SET_NULL,
    )


    def __str__(self) -> str:
        return self.source



    class Meta:
        app_label: str = 'news'
        ordering:  str = ['source']
