from django.urls import reverse_lazy
from django.views.generic import FormView, ListView, TemplateView

from .forms import MatchSelectionForm
from .models import Match, Season


class HomeAwayWidgetView(ListView):
    template_name = "matches/home_away_widget.html"

    def get_queryset(self):
        if "season" in self.request.GET:
            if self.request.GET["season"]:
                pk = int(self.request.GET["season"])
                try:
                    s = Season.objects.get(pk=pk)
                except Season.DoesNotExist:
                    return Match.objects.none()
                return s.match_set.all()
            return Match.objects.none()
        return Match.objects.all()


class MatchFormView(FormView):
    form_class = MatchSelectionForm
    template_name = "matches/match_form.html"
    success_url = reverse_lazy("match_success")

    def form_valid(self, form):
        season = form.get_season()
        home_team = form.get_home_team()
        away_team = form.get_away_team()
        match = form.get_match()
        self.request.session["cleaned_data"] = str(form.cleaned_data)
        self.request.session["season"] = str(season)
        self.request.session["home_team"] = str(home_team)
        self.request.session["away_team"] = str(away_team)
        self.request.session["match"] = str(match)
        return super().form_valid(form)


class MatchSuccessView(TemplateView):
    template_name = "matches/match_success.html"
