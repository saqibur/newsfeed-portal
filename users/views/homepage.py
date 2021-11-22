from typing import Any

from django.http import (
    HttpRequest,
    HttpResponse,
)
from django.http.response import HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy



class HomeView(TemplateView):
    template_name: str = "users/home.html"


    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        if request.user.is_anonymous:
            return HttpResponseRedirect(reverse_lazy('user:login'))
        else:
            return super().get(request, *args, **kwargs)
