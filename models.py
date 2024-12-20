from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    STATUS_CHOICES = [
        ('Upcoming', 'Upcoming'),
        ('Ongoing', 'Ongoing'),
        ('Completed', 'Completed'),
    ]
    title = models.CharField(max_length=150)
    description = models.TextField()
    location = models.CharField(max_length=200)
    date_time = models.DateTimeField()
    capacity = models.PositiveIntegerField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    attendees = models.ManyToManyField(User, related_name='events', blank=True)

    def __str__(self):
        return self.title
