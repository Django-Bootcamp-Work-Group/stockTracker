from django.db import models
from django.utils.translation import gettext_lazy as _


class ItemTypes(models.TextChoices):
    """
    Item types options
    """

    FRUIT = "fruit", _("fruit")
