from django.db import models
from django.db.models import Q

from kullanicilar.models import Kullanici
from ilaclar.models import Ilac
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator


class Stok(models.Model):
    depo = models.ForeignKey(Kullanici, on_delete=models.CASCADE)
    ilac = models.ForeignKey(Ilac, on_delete=models.CASCADE)
    adet = models.PositiveSmallIntegerField(default=1)
    kalan = models.PositiveSmallIntegerField(blank=True, null=True)
    eklenme = models.DateTimeField(auto_now_add=True)
    duzenlenme = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Stoklar"

    def __str__(self):
        return "%s" % (self.ilac)

    # @classmethod
    # def create(cls, adet):
    #     kalan = cls(kalan=adet)
    #     # do something with the book
    #     return kalan

    def get_absolute_url(self):
        return reverse('stoklar:benim-stok-list')


class Sepet(models.Model):
    eczane = models.ForeignKey(Kullanici, on_delete=models.CASCADE)
    stok = models.ForeignKey(Stok, on_delete=models.CASCADE)
    # mustahzar = models.ForeignKey(Mustahzar, on_delete=models.CASCADE)
    # mesaj = models.CharField(max_length=120, blank=True, null=True)
    adet = models.PositiveSmallIntegerField(default=1)
    eklenme = models.DateTimeField(auto_now_add=True)
    duzenlenme = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s" % (self.stok)

    class Meta:
        verbose_name_plural = "Sepetler"

    def get_absolute_url(self):
        return reverse('stoklar:benim-sepet-list')


class SepetOnay(models.Model):
    onay_secenek = (
        ('onaylandı', 'onaylandı'),
        ('reddedildi', 'reddedildi'),
    )

    depo = models.ForeignKey(Kullanici, on_delete=models.CASCADE)
    onay = models.CharField('Onay', max_length=16, choices=onay_secenek, default='onaylandı')
    sepet = models.ForeignKey(Sepet, on_delete=models.CASCADE)
    adet = models.PositiveSmallIntegerField(default=0)
    # mesaj = models.CharField(max_length=120, blank=True, null=True)
    eklenme = models.DateTimeField(auto_now_add=True)
    duzenlenme = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s" % (self.onay)

    def save(self, *args, **kwargs):
        self.sepet.stok.kalan -= self.adet
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Onaylar"

    def get_absolute_url(self):
        return reverse('stoklar:benim-onay-list')
