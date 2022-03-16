from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.response import Response
import sys
import os
from ships_tracker.ships.models import Ship, ShipMovementHistory
from ships_tracker.ships.serializers import ShipSerializer, ShipMovementHistorySerializer

token = openapi.Parameter('token', in_=openapi.IN_QUERY, type=openapi.TYPE_STRING)


class ShipViewSet(viewsets.GenericViewSet):
    queryset = Ship.objects.all()
    serializer_class = ShipSerializer

    @swagger_auto_schema(manual_parameters=[token])
    def list(self, request, *args, **kwargs):
        token = self.request.query_params.get('token')
        queryset = Ship.objects.filter(owner__token=token).all()
        serializer = ShipSerializer(queryset, many=True)
        return Response(serializer.data)


class ShipMovementHistoryViewSet(viewsets.GenericViewSet):
    queryset = ShipMovementHistory.objects.all()
    serializer_class = ShipMovementHistorySerializer

    @swagger_auto_schema(manual_parameters=[token])
    def list(self, request, *args, **kwargs):
        token = self.request.query_params.get('token')
        queryset = ShipMovementHistory.objects.filter(ship__owner__token=token).all()
        serializer = ShipMovementHistorySerializer(queryset, many=True)
        return Response(serializer.data)