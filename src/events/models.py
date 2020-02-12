from django.db import models

# Create your models here.
class Event(models.Model):
        image = models.ImageField(upload_to='images/', null=True, blank = True)
        title = models.CharField(max_length=100)
        location = models.CharField(max_length=200)
        datetime_event = models.DateTimeField()
        description = models.TextField(null=True, blank=True)
        price = models.FloatField(max_length=6)
        date_added = models.DateTimeField(auto_now_add=True)
