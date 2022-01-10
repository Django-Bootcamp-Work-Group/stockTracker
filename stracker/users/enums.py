from django.db import models
from django.utils.translation import gettext_lazy as _


class Gender(models.TextChoices):
    """
    Gender of the user
    """

    MALE = "male", _("Male")
    FEMALE = "female", _("Female")
    NOT_SPECIFIED = "not_specified", _("Not Specified")

