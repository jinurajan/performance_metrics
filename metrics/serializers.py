# posts/serializers.py
from rest_framework import serializers
from . import models


class MetricSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('date', 'channel', 'country', 'os', 'impressions', 'clicks', 'installs', 'spend', 'revenue')
        model = models.Metric