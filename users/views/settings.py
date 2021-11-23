from typing import Any

from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import QuerySet
from django.forms import Form
from django.http.response import HttpResponse
from django.views.generic.edit import FormView
from django.urls import reverse_lazy

from news.models.country import Country
from news.models.keyword import Keyword
from news.models.source import Source
from users.forms.settings import SettingsForm
from users.models.subscription import Subscription



class SettingsView(LoginRequiredMixin, FormView):
    template_name: str          = 'users/settings.html'
    login_url:     str          = 'user:login'
    form_class:    Form         = SettingsForm
    success_url:   HttpResponse = reverse_lazy('user:settings')


    def get_initial(self) -> dict[str, Any]:
        user: settings.AUTH_USER_MODEL = self.request.user

        try:
            user_subscription: Subscription = Subscription.objects.get(user=user)
        except Subscription.DoesNotExist:
            return {}

        countries_for_user: QuerySet[Country] = (
            user_subscription.countries.all()
        )

        keywords_for_user: QuerySet[Keyword] = (
            user_subscription.keywords.all()
        )

        sources_for_user: QuerySet[Source] = (
            user_subscription.sources.all()
        )

        return {
            'countries': [ country.country for country in countries_for_user ],
            'keywords': [ keyword.keyword for keyword in keywords_for_user ],
            'sources': [ source.source for source in sources_for_user ],
        }


    def get_form(self, *args, **kwargs) -> Form:
        user: settings.AUTH_USER_MODEL = self.request.user
        form: Form = super().get_form(*args, **kwargs)

        form.fields['sources'].choices  = [
            (source.source, source.source) for source in Source.objects.all()
        ]

        user_subscription: Subscription

        try:
            user_subscription = Subscription.objects.get(user=user)
        except Subscription.DoesNotExist:
            return form

        keywords_for_user: QuerySet[Keyword] = (
            user_subscription.keywords.all()
        )

        form.fields['keywords'].choices = [
            (keyword.keyword, keyword.keyword) for keyword in keywords_for_user
        ]

        return form


    def form_valid(self, form: Form) -> HttpResponse:
        user: settings.AUTH_USER_MODEL = self.request.user

        subscription, _ = Subscription.objects.get_or_create(user=user)

        subscription.countries.clear()
        for country in form.cleaned_data['countries']:
            country_model, _ = Country.objects.get_or_create(country=country)
            subscription.countries.add(country_model)

        subscription.sources.clear()
        for source in form.cleaned_data['sources']:
            source_model, _ = Source.objects.get_or_create(source=source)
            subscription.sources.add(source_model)

        subscription.keywords.clear()
        if form.cleaned_data['keyword']:
            new_keyword, _ = Keyword.objects.get_or_create(keyword=form.cleaned_data['keyword'])
            subscription.keywords.add(new_keyword)

        for keyword in form.cleaned_data['keywords']:
            keyword, _ = Keyword.objects.get_or_create(keyword=keyword)
            subscription.keywords.add(keyword)

        subscription.save()

        return super().form_valid(form)
