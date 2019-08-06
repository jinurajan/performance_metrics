# metrics/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.ListMetrics.as_view())
]