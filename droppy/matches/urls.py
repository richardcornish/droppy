from django.urls import path

from .views import HomeAwayWidgetView, MatchFormView, MatchSuccessView

urlpatterns = [
    path("home-away/", HomeAwayWidgetView.as_view(), name="home_away_widget"),
    path("success/", MatchSuccessView.as_view(), name="match_success"),
    path("", MatchFormView.as_view(), name="match_form"),
]
