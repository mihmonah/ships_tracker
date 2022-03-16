from django.db import models

from ships_tracker.users.models import ShipOwner


class DateCreatedMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата и время создания")

    class Meta:
        abstract = True


class Ship(DateCreatedMixin, models.Model):
    code = models.CharField(primary_key=True, max_length=255, unique=True, verbose_name="Код судна")
    name = models.CharField(max_length=255, verbose_name="Имя судна")
    owner = models.ForeignKey(
        ShipOwner,
        default=None,
        null=True,
        blank=True,
        related_name="ship",
        on_delete=models.CASCADE,
        verbose_name="Владелец судна"
    )

    class Meta:
        verbose_name = "Судно"
        verbose_name_plural = "Судна"


class ShipMovementHistory(DateCreatedMixin, models.Model):
    geo_datetime = models.DateTimeField(blank=True, verbose_name="Дата и время определения геопозиции судна")
    longitude = models.CharField(max_length=255, verbose_name="Долгота")
    width = models.CharField(max_length=255, verbose_name="Ширина")
    ship = models.ForeignKey(Ship, related_name="movement_history", on_delete=models.CASCADE, verbose_name="Судно")

    class Meta:
        verbose_name = "История перемещения судна"
        verbose_name_plural = "Истории перемещения судна"
