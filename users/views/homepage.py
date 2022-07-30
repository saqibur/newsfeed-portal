from typing import Any
from django.db.models.query import QuerySet

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import (
    HttpRequest,
    HttpResponse,
)
from django.http.response import HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.urls import reverse_lazy

from news.models.article import Article
from news.models.source import Source
from news.models.country import Country
from users.models.subscription import Subscription


class NewsfeedView(LoginRequiredMixin, ListView):
    model: Article = Article
    paginate_by: int = 5
    template_name: str = "users/newsfeed.html"

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        return super().get(request, *args, **kwargs)

    def get_queryset(self) -> QuerySet[Article]:
        try:
            sources: list[Source] = Subscription.objects.get(
                user=self.request.user
            ).sources.all()

            countries: list[Country] = Subscription.objects.get(
                user=self.request.user
            ).countries.all()

            return (
                Article.objects.filter(source__in=sources).all()
                | Article.objects.filter(source__country__in=countries).all()
            )

        except Subscription.DoesNotExist:
            return Article.objects.none()


class HomeView(LoginRequiredMixin, TemplateView):
    template_name: str = "users/home.html"

    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        if request.user.is_anonymous:
            return HttpResponseRedirect(reverse_lazy("user:login"))
        else:
            return super().get(request, *args, **kwargs)
