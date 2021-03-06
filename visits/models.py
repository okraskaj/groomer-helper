from django.db import models

from animals.models import Animal
from config.settings import DEFAULT_SALON_ID
from salons.models import Salon


class Visit(models.Model):
    start = models.DateTimeField(null=False)
    stop = models.DateTimeField(null=False)
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, )
    service = models.TextField(max_length=100, blank=False, null=False,
                               unique=True)
    # TODO: choice albo nawet odddzielna tabela z danymi jak np cennik itd
    happened = models.BooleanField(null=False, default=False)
    money_taken = models.PositiveIntegerField(null=True)
    notes = models.TextField(max_length=100, blank=True, null=False)
    salon = models.ForeignKey(Salon, default=DEFAULT_SALON_ID, null=False,
                              on_delete=models.CASCADE)

    def __str__(self):
        return "".join([self.animal.name, " o ", str(self.start.hour)])

    __str__.short_description = "Opis"
