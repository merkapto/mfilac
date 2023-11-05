from django.db import models
from django.contrib.auth.models import AbstractUser

class Kullanici(AbstractUser):
    gln = models.CharField(max_length=13, unique=True, help_text='Lütfen 13 haneli GLN No yazınız.', blank=True, null=True)
    
    SEHIR_SEC = (
        ('ADANA', 'ADANA'),
        ('ADIYAMAN', 'ADIYAMAN'),
        ('ANKARA', 'ANKARA'),
        ('ISTANBUL', 'ISTANBUL'),
        ('SAMSUN', 'SAMSUN'),
    )
    sehir = models.CharField(max_length=20, default='SAMSUN', choices=SEHIR_SEC)
    SIRKET_SEC = (
        ('ECZANE', 'ECZANE'),
        ('DEPO', 'DEPO')
    )
    sirket_tipi = models.CharField(max_length=7, default='ECZANE', choices=SIRKET_SEC)
    sirket_adi = models.CharField(max_length=30, help_text='Lütfen yalnızca eczane/depo adını yazınız.')
    
    # slug = models.SlugField(blank=True, null=True)
    
    cep_telefon = models.CharField(max_length=11, help_text='05xxxxxxxxx', blank=True, null=True)
    is_telefon = models.CharField(max_length=11, help_text='isteğe bağlı...', blank=True, null=True)
    adres = models.TextField(help_text='isteğe bağlı...', blank=True, null=True)
    # resim = models.FileField(blank=True, null=True, upload_to="resim/")

    def __str__(self):
        return self.username
