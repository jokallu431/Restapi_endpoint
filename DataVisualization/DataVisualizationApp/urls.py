from django.urls import path
from DataVisualizationApp import views
from .views import csv_data
urlpatterns = [
    path("", views.services, name='services'),
    path('csv-data/', csv_data, name='csv_data'),
]
