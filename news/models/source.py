from django.db.models import (
    CharField,
    Model,
)

from libraries.newsapi_service.newsapi_wrapper import get_all_sources



class Source(Model):
    source: CharField = CharField(max_length=100, primary_key=True)

    # NOTE: This needs to be called at least once-per day to update the sources
    #       list in case there's a change. Add this to your list of assumptions.
    @classmethod
    def update_sources(cls):
        sources = get_all_sources()
        for source in sources:
            source = cls(source=source.id)
            source.save()



    class Meta:
        app_label: str = 'news'
