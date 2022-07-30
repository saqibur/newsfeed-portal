from django.db.models import (
    CharField,
    Model,
)


class KeywordField(CharField):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_prep_value(self, value):
        return str(value).lower()


class Keyword(Model):
    keyword: KeywordField = KeywordField(max_length=20, primary_key=True)

    class Meta:
        app_label: str = "news"
        ordering: list[str] = ["keyword"]
