from django.db import models
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _

from core.models import BaseAbstractModel
from customusers.models import CustomUser
from items import enums


class Category(BaseAbstractModel):
    """
    Model to hold item categories (types)
    """

    name = models.CharField(max_length=255, verbose_name=_("Category Name"))

    class Meta:
        verbose_name = _("category")
        verbose_name_plural = _("categories")

    def __str__(self):
        return f"{self.name}"


class Fridge(BaseAbstractModel):
    """
    Model to hold storage locations
    """
    name = models.CharField(verbose_name=_("name"), max_length=128, unique=True)

    def __str__(self):
        return f"{self.name}"


class Shelf(BaseAbstractModel):
    """
    Model to hold storage divisions
    """
    name = models.CharField(verbose_name=_("name"), max_length=128, unique=True)
    fridge = models.ForeignKey(Fridge, verbose_name=_("Fridge"), on_delete=models.CASCADE)
    owner = models.ForeignKey(CustomUser, verbose_name=_("Owner"), on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.fridge}"


class Item(BaseAbstractModel):
    """
    Model to hold item details
    """
    sku = models.CharField(verbose_name=_("SKU"), max_length=128, unique=True)
    name = models.CharField(verbose_name=_("name"), max_length=128)
    categories = models.ManyToManyField(Category, verbose_name=_("Categories"))
    description = models.TextField(max_length=2000, verbose_name=_("Description"))
    qrcode = models.CharField(verbose_name=_("QR Code"), max_length=128)
    image = models.ImageField(verbose_name=_("Image"))
    status = models.CharField(verbose_name=_("Status"), max_length=64)
    valid_until = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = _("Item")
        verbose_name_plural = _("Items")

    def __str__(self):
        return f"{self.name} - {self.owner}"


class Stock(BaseAbstractModel):
    """
    Model to hold item stock amounts
    """
    shelf = models.ForeignKey(Shelf, verbose_name=_("Shelf"), on_delete=models.PROTECT)
    item = models.ForeignKey(Item, verbose_name=_("Item"), on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(verbose_name=_("Quantity"))

    class Meta:
        unique_together = ("shelf", "item")
        verbose_name = _("Stock")
        verbose_name_plural = _("Stocks")

    def __str__(self):
        return f"{self.item} - {self.shelf} - {self.quantity}"


class StockMovements(BaseAbstractModel):
    """
    Model to hold stock movements
    """
    movement_from = models.ForeignKey(Stock, verbose_name=_("Movement From"), on_delete=models.PROTECT, related_name="from_stock_set")
    movement_to = models.ForeignKey(Stock, verbose_name=_("Movement To"), on_delete=models.PROTECT, related_name="to_stock_set")
    movement_type = models.CharField(choices=enums.MovementTypes.choices, verbose_name=_("Movement Type"), max_length=50)
    quantity = models.PositiveSmallIntegerField(verbose_name=_("Quantity"))
    movement_time = models.DateTimeField(verbose_name=_("Movement Time"), default=now)

    class Meta:
        verbose_name = _("Stock Movement")
        verbose_name_plural = _("Stock Movements")

    def __str__(self):
        return f"{self.movement_from} to {self.movement_to}"
