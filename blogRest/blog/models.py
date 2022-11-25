from django.db import models

# Create your models here.

class Blog(models.Model):
    yazar = models.CharField(max_length=50 , verbose_name="yazar")
    baslik = models.CharField(max_length=50 , verbose_name="baslik")
    aciklama = models.CharField(max_length=100)
    metin = models.CharField(max_length=150)
    yayimlanma_tarihi = models.DateField(auto_now=True)
    yaratilma_tahrihi = models.DateField(auto_now_add=True)

