from rest_framework import serializers

from ..models import Ride

from .driver_serializer import DriverSerializer
from .passenger_serializer import PassengerSerializer


class RideResponseSerializer(serializers.ModelSerializer):

    driver = DriverSerializer(
        read_only=True
    )

    passenger = PassengerSerializer(
        read_only=True
    )

    ride_summary = serializers.SerializerMethodField()

    class Meta:
        model = Ride

        fields = [
            'id',
            'ride_id',
            'pickup_location',
            'drop_location',
            'driver',
            'passenger',
            'status',
            'fare',
            'created_at',
            'ride_summary',
        ]

        read_only_fields = [
            'id',
            'status',
            'created_at',
            'ride_summary',
        ]

    def get_ride_summary(self, obj):

        return (
            f"{obj.pickup_location} → "
            f"{obj.drop_location}"
        )