from datetime import datetime
from os import environ
from typing import (
    Any,
    Optional,
)

from newsapi import NewsApiClient

_NEWS_API_CLIENT: NewsApiClient = NewsApiClient(environ.get("NEWS_API_KEY"))


class Source:
    id: str
    name: str
    country: Optional[str]

    def __init__(self, source: dict[str, Any]):
        self.id = source["id"]
        self.name = source["name"]
        self.country = source.get("country", None)


class Article:
    source: Source
    author: str
    title: str
    description: str
    url: str
    url_to_image: str
    published_at: datetime
    content: str

    def __init__(self, article):
        self.source = Source(article["source"])
        self.author = article["author"]
        self.title = article["title"]
        self.description = article["description"]
        self.url = article["url"]
        self.url_to_image = article["urlToImage"]
        self.published_at = article["publishedAt"]
        self.content = article["content"]


class NewsAPIResults:
    articles: list[Article]
    total_results: int

    def __init__(self, total_results: int, articles: dict[str, str]):
        self.total_results = total_results
        self.articles = [Article(article) for article in articles]


def get_top_headlines(country: str = None) -> NewsAPIResults:
    news_api_results = _NEWS_API_CLIENT.get_top_headlines(country=country)

    return NewsAPIResults(
        total_results=news_api_results["totalResults"],
        articles=news_api_results["articles"],
    )


def get_all_sources() -> list[Source]:
    source_api_results = _NEWS_API_CLIENT.get_sources()

    return [Source(source) for source in source_api_results["sources"]]
