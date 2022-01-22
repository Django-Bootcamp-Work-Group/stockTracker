from django.db import models
from django.db.models import PROTECT
from django.utils.translation import gettext_lazy as _

from users.models import User


class Shelves(models.Model):
    """
    Shelves class based model
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


class ConnectionUserStorages(models.Model):
    """
    Many-To-Many relationship between shelves and users
    Class based model
    """
    user = models.ForeignKey(User, verbose_name=_("user"), on_delete=PROTECT)
    shelve = models.ForeignKey(Shelves, verbose_name=_("shelve"), on_delete=PROTECT)


