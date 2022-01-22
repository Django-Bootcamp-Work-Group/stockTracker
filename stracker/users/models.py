from django.contrib.auth import password_validation
from django.db import models

from core.models import BaseAbstractModel
from django.utils.translation import gettext_lazy as _


class User(BaseAbstractModel):
    """
    comment
    """
    first_name = models.CharField(_("first name"), max_length=150, blank=True)
    last_name = models.CharField(_("last name"), max_length=150, blank=True)
    password = models.CharField(_('password'), max_length=128)

    _password = None

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self._password is not None:
            password_validation.password_changed(self._password, self)
            self._password = None



