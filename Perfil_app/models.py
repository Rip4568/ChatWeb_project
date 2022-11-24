from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    user = models.ForeignKey(User, blank=True, null=True)
    status = models.CharField(choices=['ativo', 'offline', 'idelling'])
    
    class Meta:
        verbose_name = ("Perfil")
        verbose_name_plural = ("Perfis")

    def __str__(self):
        return f'{self.user} {self.status}'
