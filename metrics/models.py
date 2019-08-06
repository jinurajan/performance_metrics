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

    @property
    def cpi(self):
        return round(self.spend / self.installs, 2)

    def get(self, filters=None, group_by=None, sort_by=None):
        query = Metric.objects
        if filters:
            query = query.filter(**filters)
        if group_by:
            query = query.annotate(
                models.Sum('impressions'),
                models.Sum('clicks'),
                models.Sum('installs'),
                models.Sum('spend'),
                models.Sum('revenue')
            )
        if sort_by:
            query = query.order_by(*sort_by)
        return query.all()
