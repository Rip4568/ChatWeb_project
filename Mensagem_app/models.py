from django.db import models
from django.contrib.auth.models import User

class Mensagem(models.Model):
    mensagem = models.CharField(max_length=255, blank=True, null=True)
    de = models.ForeignKey(User, blank=True, null=True)
    para = models.ForeignKey(User, blank=True, null=True)

    class Meta:
        verbose_name = ("Mensagem")
        verbose_name_plural = ("Mensagens")

    def __str__(self):
        return f'de {self.de} para {self.para}'