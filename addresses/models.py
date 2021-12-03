import geocoder

from django.db import models


mapbox_access_token = 'pk.eyJ1IjoiaG91c3NhbWNoMDEiLCJhIjoiY2t2czVjYnlmMHk0OTJycXB6MzF0Y21xYyJ9.aHq_Gn0uxs5Hczf9EPwpVA'

class Address(models.Model):
    address = models.TextField()
    lat = models.FloatField(blank=True, null=True)
    long = models.FloatField(blank=True, null=True)
    img =models.ImageField(upload_to='images/%y/%m/%d')
    def save(self, *args, **kwargs):
        g = geocoder.mapbox(self.address, key=mapbox_access_token)
        g = g.latlng  # returns => [lat, long]
        self.lat = g[0]
        self.long = g[1]
        return super(Address, self).save(*args, **kwargs)

