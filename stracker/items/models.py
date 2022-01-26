from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import BaseAbstractModel
from customers.models import Customer


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
    owner = models.ForeignKey(Customer,verbose_name=_("Owner"), on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.fridge}"


class Item(BaseAbstractModel):
    """
    Model to hold item details
    """
    sku = models.CharField(verbose_name=_("SKU"), max_length=128, unique=True)
    name = models.CharField(verbose_name=_("name"), max_length=128)
    owner = models.ForeignKey(Customer, verbose_name=_("Owner"), on_delete=models.PROTECT)
    shelf = models.ForeignKey(Shelf, verbose_name=_("Shelf"), on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, verbose_name=_("Categories"))
    description = models.TextField(max_length=2000, verbose_name=_("Description"))
    qrcode = models.ImageField(verbose_name=_("QR Code"))
    image = models.ImageField(verbose_name=_("Image"))
    status = models.CharField(verbose_name=_("Status"), max_length=64)

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
