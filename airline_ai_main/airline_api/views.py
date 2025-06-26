from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import JsonResponse
from serializers import (
    PredictionInputSerializer,
    PredictionOutputSerializer,
    PredictionRequestSerializer
)
from .services import ml_service
from .models import PredictionRequest

# Create your views here.
class PredictAPIView(APIView):
    """
    API view for making predictions
    This replace our fastapi endpoint function
    """
    def post(self, request):
        """
        Handle post requests for predictions 
        similar to fastapi
        """
        try:
            # validate input data using serializer
            input_serializer = PredictionInputSerializer(data=request.data)
            if not input_serializer.is_valid():
                return Response(
                    {'error': "Invalid input data"},
                    status=status.HTTP_400_BAD_REQUEST
                )
            # GET validated data
            validated_data = input_serializer.validated_data
            # make prediction using ml service
            prediction_result = ml_service.predict(validated_data)

            # save to database
            self.save_prediction_request(validated_data, prediction_result)

            # return prediction result
            output_serializer = PredictionOutputSerializer(data= prediction_result)

            if output_serializer.is_valid():
                return Response(
                    output_serializer.data, status=status.HTTP_200_OK
                )
            else:
                return Response(
                    {'error':'Prediction Serialization failed'},
                    status = status.HTTP_500_INTERNAL_SERVER_ERROR
                )
            
        except Exception as e:
            return f"print error: {str(e)}"
        
    def save_prediction_request(self, input_data, prediction_result):