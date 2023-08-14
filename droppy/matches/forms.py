from itertools import permutations

from django import forms
from django.urls import reverse_lazy

from .models import Match, Season, Team


class MatchForm(forms.ModelForm):
    home_away = forms.ChoiceField(label="Home Team-Away Team", choices=[("", "---------")])

    class Meta:
        model = Match
        fields = ["season"]
        widgets = {
            "season": forms.Select(attrs={
                "hx-get": reverse_lazy("home_away_widget"),
                "hx-target": "#id_home_away",
            })
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if "season" in self.data:
            try:
                pk = int(self.data.get("season"))
                s = Season.objects.get(pk=pk)
                qs = s.match_set.all()
                choices = [(f"{obj.home_team.pk}-{obj.away_team.pk}", f"{obj.home_team}-{obj.away_team}") for obj in qs]
                self.fields["home_away"].choices = choices
            except:
                pass

    def get_pk(self, index):
        return int(self.cleaned_data["home_away"].split("-")[index])

    def get_team(self, pk):
        try:
            return Team.objects.get(pk=pk)
        except Team.DoesNotExist:
            return None

    def get_home_team(self, index=0):
        pk = self.get_pk(index)
        return self.get_team(pk)

    def get_away_team(self, index=1):
        pk = self.get_pk(index)
        return self.get_team(pk)
