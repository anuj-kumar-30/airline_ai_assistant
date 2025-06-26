from rest_framework import serializers
from .models import PredictionRequest

class PredictionInputSerializer(serializers.Serializer):
    """
    Serializer for validating incoming prediction requests 
    This replace's fastapi's pydantic model for request validation
    """
    airline = serializers.CharField(max_length=100)
    flight = serializers.CharField(max_length=100)
    source_city = serializers.CharField(max_length=100)
    departure_time = serializers.CharField(max_length=100)
    stops = serializers.CharField(max_length=100)
    arrival_time = serializers.CharField(max_length=100)
    destination_city = serializers.CharField(max_length=100)
    cls = serializers.CharField(max_length=100)
    duration = serializers.CharField(max_length=100)
    days_left = serializers.IntegerField()

class PredictionOutputSerializer(serializers.Serializer):
    """
    Serializer for prediction response 
    This ensures consistent API response format
    """
    price = serializers.FloatField()

class PredictionRequestSerializer(serializers.ModelSerializer):
    """
    Model serializer for database operations
    Automatically generates field based on the model
    """
    class Meta:
        model = PredictionRequest
        fields = '__all__'