from django.core.exceptions import ValidationError
from django.db import models
from kullanicilar.models import Kullanici
from ilaclar.models import Ilac
from django.urls import reverse
from django.db.models import F, Count


class Takas(models.Model):
    takas_veren = models.ForeignKey(Kullanici, on_delete=models.CASCADE)
    ilac = models.ForeignKey(Ilac, on_delete=models.CASCADE)
    adet = models.PositiveSmallIntegerField(default=1)
    kalan = models.PositiveSmallIntegerField(blank=True, null=True)
    miad = models.DateField(blank=True, null=True)
    eklenme = models.DateTimeField(auto_now_add=True)
    duzenlenme = models.DateTimeField(auto_now=True)
    izlenme = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return "%s" % (self.ilac)

    def save(self, *args, **kwargs):
        if self.kalan is None:
            self.kalan = self.adet
        super().save(*args, **kwargs)

    class Meta:
        # ordering = ['ekleyen__eczane_adi']
        ordering = ['-eklenme']
        verbose_name_plural = "Takaslar"

    def get_absolute_url(self):
        return reverse('takaslar:benim-takas-list')  # , kwargs={'pk': self.pk})


class Talep(models.Model):
    talep_eden = models.ForeignKey(Kullanici, on_delete=models.CASCADE)
    takas = models.ForeignKey(Takas, on_delete=models.CASCADE)
    adet = models.PositiveSmallIntegerField(default=1)
    # mesaj = models.CharField(max_length=120, blank=True, null=True)
    # ilac = models.ForeignKey(Ilac, on_delete=models.CASCADE)
    eklenme = models.DateTimeField(auto_now_add=True)
    duzenlenme = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s" % (self.takas)

    def takas_veren(self):
        return "%s" % (self.takas.takas_veren)

    def onay_durum(self):
        onay = self.onay_set.filter(onay__startswith="o").first()
        red = self.onay_set.filter(onay__startswith="r").first()
        if onay:
            return onay
        elif red:
            return red
        else:
            return None
        # if self.onay_set.filter(onay__startswith="o"):
        #     return "onaylandı"
        # elif self.onay_set.get(onay__startswith="r"):
        #     return "reddedildi"

    def save(self, *args, **kwargs):
        if 0 < self.adet <= self.takas.kalan:
            super(Talep, self).save(*args, **kwargs)
        # else:
        #     raise ValidationError('The pools are all full.')

    class Meta:
        ordering = ['-eklenme']
        verbose_name_plural = "Talepler"

    def get_absolute_url(self):
        return reverse('takaslar:benim-talep-list')


class Onay(models.Model):
    onay_secenek = (
        # ('beklemede', 'beklemede'),
        ('onaylandı', 'onaylandı'),
        ('reddedildi', 'reddedildi'),
    )

    onay_veren = models.ForeignKey(Kullanici, on_delete=models.CASCADE)
    onay = models.CharField('Onay', max_length=16, choices=onay_secenek, default='onaylandı')
    talep = models.ForeignKey(Talep, on_delete=models.CASCADE)
    adet = models.PositiveSmallIntegerField(default=0)
    mesaj = models.CharField(max_length=120, blank=True, null=True)
    eklenme = models.DateTimeField(auto_now_add=True)
    duzenlenme = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s" % (self.onay)

    def takas_veren(self):
        return "%s" % (self.talep.takas.takas_veren)

    def talep_adet(self):
        return "%s" % (self.talep.adet)

    def talep_eden(self):
        return "%s" % (self.talep.talep_eden)

    # def takas_kalan(self):
    #     return "%s" % self.talep.takas.kalan

    def save(self, *args, **kwargs):
        if self.talep.takas.kalan >= self.talep.adet >= self.adet > 0 and self.onay == 'onaylandı':
            self.talep.takas.kalan -= self.adet
            self.talep.takas.save()
        elif self.onay == 'reddedildi':
            self.adet = 0
        super(Onay, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-eklenme']
        verbose_name_plural = "Onaylar"

    def get_absolute_url(self):
        return reverse('takaslar:benim-onay-list')