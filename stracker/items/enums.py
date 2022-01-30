from django.db import models
from django.utils.translation import gettext_lazy as _


class MovementTypes(models.TextChoices):
    """
    Movements types of items
    """

    BUY = "buy", _("Buy")
    TRANSFER = "transfer", _("Transfer")
    USE = "use", _("Use")
    GARBAGE = "garbage", _("Garbage")
