from rest_framework import serializers
from .models import ParserSetting, WeatherKiev


class ChangeUpdateTimeSerializer(serializers.ModelSerializer):

    """Serializer to update parser time"""

    class Meta:
        model = ParserSetting
        fields = ('update_time',)
        extra_kwargs = {'update_time': {'format': '%H:%M'}}


class GetStatusParserSerializer(serializers.ModelSerializer):

    """Getting the status of a task"""

    class Meta:
        model = ParserSetting
        fields = ('status',)


class GetWeatherKievSerializer(serializers.ModelSerializer):

    """Serializer for getting weather for 5 days"""

    class Meta:
        model = WeatherKiev
        fields = '__all__'
