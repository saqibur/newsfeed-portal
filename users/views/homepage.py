from typing import Any

from django.http import (
    HttpRequest,
    HttpResponse,
)
from django.http.response import HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy



class HomeView(TemplateView):
    template_name = "users/home.html"


    def get(
        self,
        request:  HttpRequest,
        *args:    Any,
        **kwargs: Any
    ) -> HttpResponse:
        if request.user.is_anonymous:
            return HttpResponseRedirect(reverse_lazy('users:login'))
        else:
            return super().get(request, *args, **kwargs)
