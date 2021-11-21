from typing import Any

from django import http
from django.http import response
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy



class HomeView(TemplateView):
    template_name = "users/home.html"

    def get(
        self,
        request:  http.HttpRequest,
        *args:    Any,
        **kwargs: Any
    ) -> http.HttpResponse:
        if request.user.is_anonymous:
            return response.HttpResponseRedirect(reverse_lazy('users:login'))
        else:
            return super().get(request, *args, **kwargs)
