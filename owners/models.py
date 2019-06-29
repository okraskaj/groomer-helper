from django.db import models
from django.utils.translation import ugettext_lazy as _

from config.settings import DEFAULT_SALON_ID
from salons.models import Salon


class Owner(models.Model):
    full_name = models.TextField(_("full_name"), max_length=100, blank=True, null=True)
    phone_number = models.TextField(_("phone number"), max_length=20, blank=False, null=False)
    email = models.EmailField(_("email"), max_length=100, blank=True, null=True)
    location = models.TextField(_("location"), max_length=200, blank=True, null=True)
    recommended_by = models.ForeignKey('Owner', null=True, on_delete=models.CASCADE, verbose_name=_("recommended by"))
    salon = models.ForeignKey(Salon,
                              default=DEFAULT_SALON_ID,
                              null=False,
                              on_delete=models.CASCADE,
                              verbose_name=_("salon") )

    # field to reward people with most recomendations as well as to remember people correctly
    # TODO: integrate with facebook - load image picture on creation and load additional data (likes?).

    def __str__(self):
        return "".join(self.full_name)
