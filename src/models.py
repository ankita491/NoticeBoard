from django.db import models

# Create your models here.

class Event(models.Model):
	event_name = models.CharField(max_length = 75)
	event_description = models.CharField(max_length = 1000)
	event_date = models.DateField()
	event_timing = models.TimeField()
	event_fees = models.IntegerField(default = 0)
	event_seats = models.IntegerField(default = 36)
	event_organiser_details = models.CharField(max_length = 300)


