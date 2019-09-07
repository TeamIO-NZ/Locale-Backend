from django.db import models
from django.urls import reverse

# Create your models here.

class Day(models.Model):
    
    title = models.CharField(max_length=200)
    description = models.TextField();
    date = models.DateField();

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('home')

class Event(models.Model):
    
    title = models.CharField(max_length=200)
    description = models.TextField();
    start_time = models.TimeField();
    end_time = models.TimeField();
    location = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    day = models.ForeignKey(Day, on_delete=models.CASCADE, related_name='events')
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('day', args=[str(day.id)])