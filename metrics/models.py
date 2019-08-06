import datetime
from django.db import models

class Round(models.Func):
    """
    Func Expression to round of cpi to 2 decimal values
    """
    function = 'ROUND'
    template = '%(function)s(%(expressions)s, 2)'



class Metric(models.Model):
    """
    ORM Model Definition for Metric
    """
    date = models.DateField(default=datetime.date.today)
    channel = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    os = models.CharField(max_length=10)
    impressions = models.IntegerField(default=0)
    clicks = models.IntegerField(default=0)
    installs = models.IntegerField(default=0)
    spend = models.FloatField(default=0)
    revenue = models.FloatField(default=0)

    def get(self, filters=None, group_by=None, sort_by=None):
        query = Metric.objects
        query = query.annotate(
            cpi=Round(models.ExpressionWrapper(
                models.Sum('spend') / models.Sum('installs'),
                output_field=models.FloatField())))
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
