from itertools import permutations

from django import forms
from django.urls import reverse_lazy

from .models import Match, Team


def get_home_away_choices():
    iterable = Team.objects.values_list("pk", "name")
    perms = permutations(iterable, r=2)
    choices = [(f"{perm[0][0]}-{perm[1][0]}", f"{perm[0][1]}-{perm[1][1]}") for perm in perms]
    return choices


class MatchForm(forms.ModelForm):
    home_away = forms.ChoiceField(label="Home Team-Away Team", choices=get_home_away_choices)

    class Meta:
        model = Match
        fields = ["season"]

    def get_pk(self, index):
        return self.cleaned_data["home_away"].split("-")[index]

    def get_team(self, pk):
        try:
            return Team.objects.get(pk=pk)
        except Team.DoesNotExist:
            return None

    def get_home_team(self):
        home_pk = self.get_pk(0)
        return self.get_team(home_pk)

    def get_away_team(self):
        away_pk = self.get_pk(1)
        return self.get_team(away_pk)
