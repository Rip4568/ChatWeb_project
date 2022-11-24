from django.db import models
from django.contrib.auth.models import User

class Amigo(models.Model):
    amigo = models.ForeignKey(User, blank=True, null=True)
    amigo_de = models.ForeignKey(User, blank=True, null=True)

    class Meta:
        verbose_name = ("Amigo")
        verbose_name_plural = ("Amigos")

    def __str__(self):
        return f'amigo: {self.amigo} de {self.amigo_de}'