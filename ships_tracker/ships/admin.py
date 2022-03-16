from django.contrib import admin

from ships_tracker.ships.models import Ship, ShipMovementHistory
from ships_tracker.users.models import ShipOwner


@admin.register(Ship)
class ShipAdmin(admin.ModelAdmin):
    fields = ['code', 'name', 'owner']


@admin.register(ShipOwner)
class ShipOwnerAdmin(admin.ModelAdmin):
    fields = ['username', 'token', 'password', 'is_active']
    readonly_fields = ['token']


@admin.register(ShipMovementHistory)
class ShipMovementHistoryAdmin(admin.ModelAdmin):
    pass
