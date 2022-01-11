from django.db import models
from django.utils.translation import gettext_lazy as _
from core.models import BaseAbstractModel


class Storage(BaseAbstractModel):

    """
    Storage model
    """
    number = models.IntegerField(default=0, verbose_name=_("Number"))
    description = models.CharField(max_length=500, blank=True, null=True, verbose_name=_("Description"))
    location = models.CharField(max_length=150, blank=True, verbose_name=_("Location"))

    class Meta:
        verbose_name = _("storage")
        verbose_name_plural = _("storages")

    def __str__(self):

        return f"{self.number}, {self.description}, {self.location}, "