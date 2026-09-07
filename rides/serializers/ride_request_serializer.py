from rest_framework import serializers

from ..models import Ride


class RideRequestSerializer(serializers.ModelSerializer):

    secret_code = serializers.CharField(
        write_only=True,
        required=False
    )

    class Meta:
        model = Ride

        fields = [
            'ride_id',
            'pickup_location',
            'drop_location',
            'driver',
            'passenger',
            'fare',
            'secret_code',
        ]

    def validate_fare(self, value):

        if value <= 0:
            raise serializers.ValidationError(
                "Fare must be greater than 0."
            )

        return value

    def validate(self, data):

        if data['pickup_location'] == data['drop_location']:
            raise serializers.ValidationError(
                "Pickup and drop locations cannot be the same."
            )

        return data