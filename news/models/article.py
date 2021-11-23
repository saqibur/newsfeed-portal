from django.db.models import (
    CharField,
    DateTimeField,
    ForeignKey,
    Model,
    URLField,
    CASCADE,
)

from news.models.source import Source



class Article(Model):
    title:        CharField     = CharField(max_length=300)
    author:       CharField     = CharField(max_length=500, blank=True, null=True)
    description:  CharField     = CharField(max_length=500, blank=True, null=True)
    url:          URLField      = URLField(max_length=500, blank=True, null=True)
    url_to_image: URLField      = URLField(max_length=500, blank=True, null=True)
    published_at: DateTimeField = DateTimeField(blank=True, null=True)
    content:      CharField     = CharField(max_length=220, blank=True, null=True)

    source: ForeignKey = ForeignKey(to=Source, on_delete=CASCADE)


    def __str__(self) -> str:
        return self.title



    class Meta:
        app_label: str = 'news'
        ordering: list[str] = ['-published_at']
