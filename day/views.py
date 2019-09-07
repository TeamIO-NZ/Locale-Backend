from django.views.generic import ListView
from django.views.generic.edit import CreateView

from .models import Day, Event

# Create your views here.

class DayListView(ListView):
    model = Day
    template_name = 'home.html'

class EventListView(ListView):
    model = Event
    template_name = 'day.html'

class DayCreateView(CreateView):
    model = Day
    template_name = 'day_new.html'
    fields = ['title', 'description', 'date']

class EventCreateView(CreateView):
    model = Event
    template_name = 'event_new.html'
    fields = ['day', 'title', 'description', 'start_time', 'end_time', 'location', 'price']