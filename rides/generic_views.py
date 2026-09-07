from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework.generics import (
    GenericAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)

from rest_framework.viewsets import (
    ViewSet,
    ModelViewSet,
)

from .models import Ride

from .serializers import (
    RideRequestSerializer,
    RideResponseSerializer,
)


# =====================================================
# 1. APIView
# =====================================================

class RideAPIView(APIView):

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

        serializer = RideRequestSerializer(
            data=request.data
        )

        if serializer.is_valid():

            ride = serializer.save()

            response_serializer = RideResponseSerializer(
                ride
            )

            return Response(
                response_serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


# =====================================================
# 2. GenericAPIView
# =====================================================

class RideGenericAPIView(GenericAPIView):

    queryset = Ride.objects.select_related(
        'driver',
        'passenger'
    ).all()

    def get(self, request):

        rides = self.get_queryset()

        serializer = RideResponseSerializer(
            rides,
            many=True
        )

        return Response(serializer.data)

    def post(self, request):

        serializer = RideRequestSerializer(
            data=request.data
        )

        if serializer.is_valid():

            ride = serializer.save()

            response_serializer = RideResponseSerializer(
                ride
            )

            return Response(
                response_serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


# =====================================================
# 3. ListCreateAPIView
# =====================================================

class RideListCreateAPIView(ListCreateAPIView):

    queryset = Ride.objects.select_related(
        'driver',
        'passenger'
    ).all()

    def get_serializer_class(self):

        if self.request.method == 'POST':
            return RideRequestSerializer

        return RideResponseSerializer


# =====================================================
# 4. RetrieveUpdateDestroyAPIView
# =====================================================

class RideDetailAPIView(
    RetrieveUpdateDestroyAPIView
):

    queryset = Ride.objects.select_related(
        'driver',
        'passenger'
    ).all()

    def get_serializer_class(self):

        if self.request.method in [
            'PUT',
            'PATCH',
        ]:
            return RideRequestSerializer

        return RideResponseSerializer


# =====================================================
# 5. ViewSet
# =====================================================

class RideViewSet(ViewSet):

    def list(self, request):

        rides = Ride.objects.select_related(
            'driver',
            'passenger'
        ).all()

        serializer = RideResponseSerializer(
            rides,
            many=True
        )

        return Response(serializer.data)

    def retrieve(self, request, pk=None):

        try:
            ride = Ride.objects.select_related(
                'driver',
                'passenger'
            ).get(pk=pk)

        except Ride.DoesNotExist:

            return Response(
                {
                    'error': 'Ride not found'
                },
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = RideResponseSerializer(ride)

        return Response(serializer.data)

    def create(self, request):

        serializer = RideRequestSerializer(
            data=request.data
        )

        if serializer.is_valid():

            ride = serializer.save()

            response_serializer = RideResponseSerializer(
                ride
            )

            return Response(
                response_serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


# =====================================================
# 6. ModelViewSet
# =====================================================

class RideModelViewSet(ModelViewSet):

    queryset = Ride.objects.select_related(
        'driver',
        'passenger'
    ).all()

    def get_serializer_class(self):

        if self.action in [
            'create',
            'update',
            'partial_update',
        ]:
            return RideRequestSerializer

        return RideResponseSerializer