from django.db import models
from django.forms import CharField, ImageField

# Create your models here.

class Karte(models.Model):
    ime= models.CharField(max_length=50)
    slika = models.ImageField(upload_to='slike', null=True)
    tekst = models.TextField(max_length=200)
    vrijeme=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.ime