from django.urls import path

from .views import TripWidgetView, TripFormView, TripSuccessView

urlpatterns = [
    path("cities/", TripWidgetView.as_view(), name="trip_widget"),
    path("success/", TripSuccessView.as_view(), name="trip_success"),
    path("", TripFormView.as_view(), name="trip_form"),
]
