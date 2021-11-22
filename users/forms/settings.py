from django.forms import (
    CharField,
    CheckboxSelectMultiple,
    Form,
    MultipleChoiceField,
)
from libraries.newsapi_service.countries import Country



class SettingsForm(Form):
    countries: MultipleChoiceField = MultipleChoiceField(
        choices  = Country.choices(),
        widget   = CheckboxSelectMultiple(),
        required = False,
    )

    keywords: MultipleChoiceField = MultipleChoiceField(
        widget   = CheckboxSelectMultiple(),
        required = False,
    )

    sources: MultipleChoiceField = MultipleChoiceField(
        widget   = CheckboxSelectMultiple(),
        required = False,
    )

    keyword: CharField = CharField(
        max_length = 20,
        required   = False,
    )
