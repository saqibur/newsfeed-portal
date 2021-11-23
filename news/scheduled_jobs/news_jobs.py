from libraries.newsapi_service.newsapi_wrapper import (
    NewsAPIResults,
    get_top_headlines,
    get_all_sources,
)

from news.models.article import Article as NewsArticle
from news.models.source import Source
from news.models.country import Country
from users.models.subscription import Subscription

def _notify_subscribers(article: NewsArticle):
    subscriptions = Subscription.objects.all()

    for subscription in subscriptions:
        keywords: list[str] = [
            keyword.keyword for keyword in subscription.keywords.all()
        ]

        if any(word.lower() in article.title for word in keywords):
            # TODO: Should send a single email for all relevant articles found.
            print("Sending email to", subscription.user)


def fetch_top_headlines_job():
    top_headlines: NewsAPIResults = get_top_headlines()

    for article in top_headlines.articles:
        source, _ = Source.objects.get_or_create(
                source = article.source.name,
        )

        news_article, added = NewsArticle.objects.get_or_create(
            title        = article.title,
            author       = article.author,
            description  = article.description,
            url          = article.url,
            url_to_image = article.url_to_image,
            published_at = article.published_at,
            content      = article.content,
            source       = source,
        )

        if added:
            _notify_subscribers(news_article)


def update_sources_job():
    for source in get_all_sources():
        country, _ = Country.objects.get_or_create(country = source.country)

        _, _ = Source.objects.update_or_create(
            source   = source.name,
            defaults = { 'country': country },
        )
