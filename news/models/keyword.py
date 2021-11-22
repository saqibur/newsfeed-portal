from django.db.models import (
    CharField,
    Model,
)



class Keyword(Model):
    keyword: CharField = CharField(max_length=20, primary_key=True)



    class Meta:
        app_label: str = 'news'
