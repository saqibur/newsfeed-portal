from django.contrib import admin
from news.models.article import Article
from news.models.country import Country
from news.models.keyword import Keyword
from news.models.source import Source



@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['published_at', 'title']
    list_filter  = ['source']



@admin.register(Source)
class SourceAdmin(admin.ModelAdmin):
    list_display = ['source', 'country']
    list_filter  = ['country']



admin.site.register(Country)
admin.site.register(Keyword)
