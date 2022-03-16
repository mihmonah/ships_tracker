from django.urls import include, path

from ships_tracker.ships.routers import root_router, movement_history_router

ships_urlpattern = [
    path('', include(root_router.urls)),
    path('', include(movement_history_router.urls)),
]
