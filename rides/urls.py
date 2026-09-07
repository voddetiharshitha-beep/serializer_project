from django.urls import include, path

from .views import RideListCreateAPIView
from rest_framework.routers import DefaultRouter

from .generic_views import (
    RideAPIView,
    RideGenericAPIView,
    RideListCreateAPIView,
    RideDetailAPIView,
    RideViewSet,
    RideModelViewSet,
)

# =====================================================
# Router
# =====================================================

router = DefaultRouter()

router.register(
    'viewset/rides',
    RideViewSet,
    basename='ride-viewset'
)

router.register(
    'modelviewset/rides',
    RideModelViewSet,
    basename='ride-modelviewset'
)

urlpatterns = [

    path(
        '',
        RideListCreateAPIView.as_view(),
        name='ride-list-create'
    ),
     # APIView
    path(
        'apiview/rides/',
        RideAPIView.as_view(),
        name='ride-apiview'
    ),
 # GenericAPIView
    path(
        'generic/rides/',
        RideGenericAPIView.as_view(),
        name='ride-generic'
    ),

    # ListCreateAPIView
    path(
        'list-create/rides/',
        RideListCreateAPIView.as_view(),
        name='ride-list-create'
    ),

    # RetrieveUpdateDestroyAPIView
    path(
        'detail/rides/<int:pk>/',
        RideDetailAPIView.as_view(),
        name='ride-detail'
    ),
      # ViewSet + ModelViewSet
    path(
        '',
        include(router.urls)
    ),

]