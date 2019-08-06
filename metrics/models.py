import datetime
from django.db import models

# Create your models here.


class Metric(models.Model):
    date = models.DateField(default=datetime.date.today)
    channel = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    os = models.CharField(max_length=10)
    impressions = models.IntegerField(default=0)
    clicks = models.IntegerField(default=0)
    installs = models.IntegerField(default=0)
    spend = models.FloatField(default=0)
    revenue = models.FloatField(default=0)

    def __str__(self):
        # return {
        #     "date": self.date,
        #     "channel": self.channel,
        #     "country": self.country,
        #     "os": self.os,
        #     "impressions": self.impressions,
        #     "clicks": self.clicks,
        #     "installs": self.installs,
        #     "spend": self.spend,
        #     "revenue": self.revenue
        # }
        return self.channel
