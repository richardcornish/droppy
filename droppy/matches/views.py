from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView

from .forms import MatchForm


class MatchFormView(FormView):
    form_class = MatchForm
    template_name = "matches/match_form.html"
    success_url = reverse_lazy("match_success")

    def form_valid(self, form):
        self.request.session["cleaned_data"] = str(form.cleaned_data)
        self.request.session["home_team"] = str(form.get_home_team())
        self.request.session["away_team"] = str(form.get_away_team())
        return super().form_valid(form)


class MatchSuccessView(TemplateView):
    template_name = "matches/match_success.html"
