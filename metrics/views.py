# posts/views.py
from rest_framework import generics

from .models import Metric
from .serializers import MetricSerializer


class MetricList(generics.ListAPIView):
    queryset = Metric.objects.all()
    serializer_class = MetricSerializer
