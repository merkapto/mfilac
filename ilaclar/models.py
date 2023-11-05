from django.db import models
from django.contrib import admin

class EtkenMadde(models.Model):
	etken_madde_adi = models.CharField(max_length=32)
	# ilac = models.ForeignKey('Ilac', on_delete=models.CASCADE)
	def __str__(self):
		return self.etken_madde_adi
	class Meta:
		ordering = ['etken_madde_adi']
		verbose_name = "Etken Madde"
		verbose_name_plural = "Etken Maddeler"
		
def ilac_resim_yeri(instance, filename):
	filebase, extension = filename.split(".")
	return "%s/%s.%s" %(instance.ilac, instance, extension)
	#return "%s/%s" %(instance.id, instance)
    
class Ilac(models.Model):
	ilac_adi = models.CharField(max_length=64)
	# etkenmadde = models.ForeignKey('EtkenMadde', on_delete=models.CASCADE)
	etkenmadde = models.ManyToManyField('EtkenMadde', blank=True)
	resim = models.FileField(upload_to=ilac_resim_yeri, blank=True, null=True)
	# firma = models.CharField('Firma', max_length=32, blank=True, null=True)
	# barkod = models.CharField('Barkod', max_length=13, blank=True, null=True)
	# karekod = models.CharField('Karekod', max_length=40, blank=True, null=True)
	# muadil = models.ManyToManyField("self", blank=True)
	# yakin_muadil = models.ManyToManyField("self", blank=True)
	aktif = models.BooleanField(default=True)
	
	
	def __str__(self):
		return self.ilac_adi
	
	@admin.display(description='etkenmadde')
	def get_etkenmadde(self):
		return [i.etken_madde_adi for i in self.etkenmadde.all()]
	
	class Meta:
		ordering = ['ilac_adi']
		verbose_name = "İlaç"
		verbose_name_plural = "İlaçlar"
	