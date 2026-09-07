from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Ride

from .serializers import (
    RideRequestSerializer,
    RideResponseSerializer,
)


class RideListCreateAPIView(APIView):

    def get(self, request):

        rides = Ride.objects.select_related(
            'driver',
            'passenger'
        ).all()

        serializer = RideResponseSerializer(
            rides,
            many=True
        )

        return Response(serializer.data)

    def post(self, request):

        request_serializer = RideRequestSerializer(
            data=request.data
        )

        if request_serializer.is_valid():

            ride = request_serializer.save()

            response_serializer = RideResponseSerializer(
                ride
            )

            return Response(
                response_serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            request_serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )