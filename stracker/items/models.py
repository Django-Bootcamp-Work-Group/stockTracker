from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import BaseAbstractModel
from items import enums


class Items(BaseAbstractModel):
    """
    Class based Items model
    type is Charfield with choices comes from enums.py
    """
    name = models.CharField(_("name"), max_length=150, null=False, blank=False)
    type = status = models.CharField(
        choices=enums.ItemTypes.choices,
        default=enums.ItemTypes.FRUIT,
        max_length=30,
        verbose_name=_("Types"),
    )
    description = models.CharField(_("description"), max_length=250, null=False , blank=False)
    barcode = models.CharField(_("barcode"), max_length=128, null=False, blank=False)
    image = models.ImageField(upload_to='media/% Y/% m/% d/', height_field=None, width_field=None, max_length=100)
    status = models.BooleanField(_("status"), null=False, blank=False)

    def __str__(self):
        return f"{self.name}"
