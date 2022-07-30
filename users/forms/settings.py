from django.forms import (
    CharField,
    CheckboxSelectMultiple,
    Form,
    MultipleChoiceField,
    ModelMultipleChoiceField,
)

from news.models.country import Country


class SettingsForm(Form):
    countries: ModelMultipleChoiceField = ModelMultipleChoiceField(
        queryset=Country.objects.all(),
        widget=CheckboxSelectMultiple(),
        required=False,
    )

    keywords: MultipleChoiceField = MultipleChoiceField(
        widget=CheckboxSelectMultiple(),
        required=False,
    )

    sources: MultipleChoiceField = MultipleChoiceField(
        widget=CheckboxSelectMultiple(),
        required=False,
    )

    keyword: CharField = CharField(
        max_length=20,
        required=False,
    )
