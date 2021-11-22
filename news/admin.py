from django.contrib import admin
from news.models.article import Article
from news.models.country import Country
from news.models.keyword import Keyword
from news.models.source import Source

admin.site.register(Article)
admin.site.register(Country)
admin.site.register(Keyword)
admin.site.register(Source)
