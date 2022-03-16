from django.contrib import admin
from ships_tracker.users.models import ShipOwner


class ShipOwnerAdmin(admin.StackedInline):
    model = ShipOwner
    fields = ['username', 'token', 'is_active']
