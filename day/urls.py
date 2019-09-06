from django.urls import path

from .views import DayListView, EventListView

urlpatterns = [
    path('', DayListView.as_view(), name='home'),
    path('day/<int:pk>/', EventListView.as_view(), name='day'),
]