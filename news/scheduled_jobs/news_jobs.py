from libraries.newsapi_service.newsapi_wrapper import (
    Article,
    NewsAPIResults,
    get_top_headlines,
    get_all_sources,
)

from news.models.article import Article as NewsArticle
from news.models.source import Source
from users.models.subscription import Subscription

def _notify_subscribers(article: NewsArticle):
    subscriptions = Subscription.objects.all()

    for subscription in subscriptions:
        keywords: list[str] = [
            keyword.keyword for keyword in subscription.keywords.all()
        ]

        if any(word in article.title for word in keywords):
            print("Sending email to", subscription.user)


def fetch_top_headlines_job():
    top_headlines: NewsAPIResults = get_top_headlines()
    articles: list[Article] = top_headlines.articles

    for article in articles:
        source, _ = Source.objects.get_or_create(
                source = article.source.name
        )

        article, added = NewsArticle.objects.get_or_create(
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
            _notify_subscribers(article)


def update_sources_job():
    sources = get_all_sources()
    for source in sources:
        source = Source(source=source.name)
        source.save()
