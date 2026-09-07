from rest_framework import serializers

from ..models import Ride


class DynamicRideSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ride

        fields = [
            'id',
            'ride_id',
            'pickup_location',
            'drop_location',
            'status',
            'fare',
            'created_at',
        ]

    def __init__(self, *args, **kwargs):

        fields = kwargs.pop('fields', None)

        super().__init__(*args, **kwargs)

        if fields is not None:

            allowed_fields = set(fields)

            existing_fields = set(self.fields)

            for field_name in existing_fields - allowed_fields:
                self.fields.pop(field_name)