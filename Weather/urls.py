from django.urls import path
from .views import *


urlpatterns = [
    path('api/change-time-update', ChangeUpdateTimeView.as_view(), name='change-time-update'), #change parser start time
    path('api/get-weather-kiev', GetWeatherView.as_view(), name='get-weather-kiev'), #getting weather records
    path('api/get-status-parser', GetStatusParserView.as_view(), name='get-status-parser'), #checking execution status
    path('api/run-parser', RunParserView.as_view(), name='run-parser') #launching the parser with a get request
]