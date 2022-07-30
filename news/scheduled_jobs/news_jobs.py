from django.conf import settings
from django.template import loader

from libraries.newsapi_service.newsapi_wrapper import (
    NewsAPIResults,
    get_top_headlines,
    get_all_sources,
)
from libraries.sendgrid_service.sendgrid_service import send_email
from news.models.article import Article as NewsArticle
from news.models.source import Source
from news.models.country import Country
from users.models.subscription import Subscription


def _notify_subscribers(articles: list[NewsArticle]):
    subscriptions = Subscription.objects.all()

    for subscription in subscriptions:
        keywords: list[str] = [
            keyword.keyword for keyword in subscription.keywords.all()
        ]

        def is_article_notable(article):
            return any(word.lower() in str(article.title).lower() for word in keywords)

        notable_articles = [
            article for article in articles if is_article_notable(article)
        ]

        html_content = loader.render_to_string(
            "users/newsfeed_email.html",
            {"articles": notable_articles},
        )

        if not notable_articles == []:
            send_email(
                from_email=settings.FROM_EMAIL,
                to_email=subscription.user.email,
                html_content=html_content,
                subject="Newsfeed Notification from Newsfeed-Portal",
            )


def fetch_top_headlines_job():
    top_headlines: NewsAPIResults = get_top_headlines()

    new_articles = []

    for article in top_headlines.articles:
        source, _ = Source.objects.get_or_create(
            source=article.source.name,
        )

        news_article, added = NewsArticle.objects.get_or_create(
            title=article.title,
            author=article.author,
            description=article.description,
            url=article.url,
            url_to_image=article.url_to_image,
            published_at=article.published_at,
            content=article.content,
            source=source,
        )

        if added:
            new_articles.append(news_article)

    if not news_article == []:
        _notify_subscribers(new_articles)


def update_sources_job():
    for source in get_all_sources():
        country, _ = Country.objects.get_or_create(country=source.country)

        _, _ = Source.objects.update_or_create(
            source=source.name,
            defaults={"country": country},
        )
