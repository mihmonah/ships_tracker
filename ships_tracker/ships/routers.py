from rest_framework import routers

from ships_tracker.ships import views

root_router = routers.DefaultRouter()
root_router.register(r'ships', views.ShipViewSet, basename='ships')

movement_history_router = routers.DefaultRouter()
movement_history_router.register(r'movement_history', views.ShipMovementHistoryViewSet, basename='movement_history')
