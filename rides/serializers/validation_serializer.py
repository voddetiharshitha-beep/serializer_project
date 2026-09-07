from rest_framework import serializers


class RideValidationSerializer(serializers.Serializer):

    pickup_location = serializers.CharField(
        max_length=200
    )

    drop_location = serializers.CharField(
        max_length=200
    )

    fare = serializers.DecimalField(
        max_digits=10,
        decimal_places=2
    )

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