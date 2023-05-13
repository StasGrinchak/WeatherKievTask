from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ChangeUpdateTimeSerializer, GetWeatherKievSerializer, GetStatusParserSerializer
from .models import ParserSetting, WeatherKiev
from Server.tasks import parser


class ChangeUpdateTimeView(APIView):

    """Change parser start time on a daily basis"""

    def put(self, request, format=None):
        time = ParserSetting.objects.all().first()
        serializer = ChangeUpdateTimeSerializer(time, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetWeatherView(APIView):

    """Getting the last five weather records from the database"""

    def get(self, request, format=None):
        weather = WeatherKiev.objects.all().order_by('-id')[:5]
        reverse_entry = reversed(weather)
        serializer = GetWeatherKievSerializer(reverse_entry, many=True)
        return Response(serializer.data)
    

class GetStatusParserView(APIView):

    """Get parser execution status"""

    def get(self, request, format=None):
        status = ParserSetting.objects.all().first()
        serializer = GetStatusParserSerializer(status)
        return Response(serializer.data)
    

class RunParserView(APIView):

    """Instant launch of the parser regardless of time"""

    def get(self, request, format=None):
        parser()
        return  Response({'message': 'Parser is running!'})
