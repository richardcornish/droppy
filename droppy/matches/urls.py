from django.urls import path

from .views import MatchFormView, MatchSuccessView

urlpatterns = [
    path("success/", MatchSuccessView.as_view(), name="match_success"),
    path("", MatchFormView.as_view(), name="match_form"),
]
