from typing import Any

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
from users.models.subscription import Subscription



class NewsfeedView(ListView):
    model         = Article
    paginate_by   = 10
    template_name = 'users/newsfeed.html'

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        sources: list[Source] = (
            Subscription.objects.get(user=self.request.user).sources.all()
        )

        return Article.objects.filter(source__in=sources).all()



class HomeView(TemplateView):
    template_name: str = "users/home.html"


    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        if request.user.is_anonymous:
            return HttpResponseRedirect(reverse_lazy('user:login'))
        else:
            return super().get(request, *args, **kwargs)
