from django.urls import reverse_lazy
from django.views.generic import FormView, ListView, TemplateView

from .forms import TripForm
from .models import Trip


class TripWidgetView(ListView):
    template_name = "trips/trip_widget.html"

    def get_queryset(self):
        if "country" in self.request.GET:
            if self.request.GET["country"]:
                country = self.request.GET["country"]
                return Trip.objects.filter(country=country).order_by("departure")
            return Trip.objects.none()
        return Trip.objects.all()


class TripFormView(FormView):
    form_class = TripForm
    template_name = "trips/trip_form.html"
    success_url = reverse_lazy("trip_success")

    def form_valid(self, form):
        self.request.session["cleaned_data"] = str(form.cleaned_data)
        return super().form_valid(form)


class TripSuccessView(TemplateView):
    template_name = "trips/trip_success.html"
