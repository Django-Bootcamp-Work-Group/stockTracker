from django.db import models
from django.db.models import PROTECT
from django.utils.translation import gettext_lazy as _

from core.models import BaseAbstractModel
from items.models import Items
from shelves.models import ConnectionUserStorages


class ItemLocations(models.Model):
    """
    commend
    """
    connection = models.ForeignKey(ConnectionUserStorages, verbose_name=_("Connection"), on_delete=PROTECT)
    item = models.ForeignKey(Items, verbose_name=_("Items"), on_delete=PROTECT)
    quantity = models.PositiveIntegerField(_("quantity"), null=False, blank=True, default=0)


class StockMovements(BaseAbstractModel):
    """
    commend
    """
    direction = models.IntegerField(_("direction"), null=False, blank=False)
    item_location = models.ForeignKey(ItemLocations, verbose_name=_("item location"), on_delete=PROTECT)
    quantity = models.PositiveIntegerField(_("quantity"), null=False, blank=True, default=0)

