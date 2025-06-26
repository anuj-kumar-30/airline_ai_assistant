from django.db import models

# Create your models here.
class PredictionRequest(models.Model):
    airline = models.CharField(max_length=100, default='SpiceJet') # name of flight
    flight = models.CharField(max_length=100, default='SG-8709')
    source_city = models.CharField(max_length=100, default='Delhi')
    departure_time = models.CharField(max_length=100, default="Evening")
    stops = models.CharField(max_length=100, default='zero')
    arrival_time = models.CharField(max_length=100, default='Night')
    destination_city = models.CharField(max_length=100, default='Mumbai')
    cls = models.CharField(max_length=100, default="Economy")
    duration = models.CharField(max_length=100, default="2.17")
    days_left = models.IntegerField(default=1)

    price = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'pridiction_request'
    def __str__(self):
        return f"{self.airline} --> {self.price}"