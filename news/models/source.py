from django.db.models import (
    CharField,
    Model,
)



class Source(Model):
    source: CharField = CharField(max_length=100, primary_key=True)



    class Meta:
        app_label: str = 'news'
