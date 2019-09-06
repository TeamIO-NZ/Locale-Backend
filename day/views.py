from django.views.generic import ListView

from .models import Day, Event

# Create your views here.

class DayListView(ListView):
    model = Day
    template_name = 'home.html'

class EventListView(ListView):
    model = Event
    template_name = 'day.html'