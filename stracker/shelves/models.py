from django.db import models
from django.utils.translation import gettext_lazy as _


class Shelves(models.Model):
    """
    commend
    """
    number = models.PositiveIntegerField(_("number"), null=False, blank=False)
    description = models.CharField(_("description"), max_length=250, null=False, blank=False)
    location = models.CharField(_("location"), max_length=250, null=False, blank=False)
    status = models.BooleanField(_("status"), null=False, blank=False)

    class Meta:
        verbose_name = _("shelve")
        verbose_name_plural = _("shelves")

    def __str__(self):
        return f"{self.number} {self.description}"

