from django.views.generic import ListView

from .models import Day

# Create your views here.

class DayListView(ListView):
    model = Day
    template_name = 'home.html'