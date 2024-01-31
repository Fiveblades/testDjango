from django.db import models
from django.conf import settings
from django.utils import timezone


class Post(models.Model):
    voetballer_naam = models.CharField(max_length=100)
    voetbalclub = models.CharField(max_length=100)
    auteur_naam = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='voetbalspeler_posts')
    datum_invoer = models.DateTimeField(default=timezone.now)
    datum_wijziging = models.DateTimeField(blank=True, null=True)


def __str__(self):
    return f"{self.voetballer_naam} - {self.voetbalclub}"
