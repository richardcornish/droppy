from django import forms
from django.urls import reverse_lazy

from .models import Trip

class TripForm(forms.Form):
    country = forms.ModelChoiceField(queryset=Trip.objects.values_list("country", flat=True).distinct(), widget=forms.Select(attrs={
        "hx-get": reverse_lazy("trip_widget"),
        "hx-target": "#id_trip",
    }))
    trip = forms.ModelChoiceField(queryset=Trip.objects.none())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if "country" in self.data and "trip" in self.data:
            pk = int(self.data["trip"])
            try:
                qs = Trip.objects.filter(pk=pk)
                self.fields["trip"].queryset = qs
                del self.fields["country"]  # discarded because `trip` field has country
            except Trip.DoesNotExist:
                pass
