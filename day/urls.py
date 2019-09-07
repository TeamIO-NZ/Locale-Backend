from django.urls import path

from .views import DayListView, EventListView, DayCreateView, EventCreateView

urlpatterns = [
    path('day/new', DayCreateView.as_view(), name='day_new'),
    path('day/<int:pk>/', EventListView.as_view(), name='day'),
    path('day/<int:pk>/new', EventCreateView.as_view(), name='event_new'),
    path('', DayListView.as_view(), name='home'),
]