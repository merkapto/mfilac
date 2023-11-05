from django.contrib import admin

from .models import Stok, Sepet, SepetOnay

class StokAdmin(admin.ModelAdmin):
    list_display = ('ilac', 'adet', 'kalan', 'depo', 'eklenme', 'duzenlenme', 'id', )
    list_per_page = 20
    list_filter = ('ilac', 'depo', )
    class Meta:
        model = Stok

class SepetAdmin(admin.ModelAdmin):
    list_display = ('stok', 'adet', 'eczane', 'eklenme', 'duzenlenme', 'id', )
    list_per_page = 20
    list_filter = ('stok', 'eczane', )
    class Meta:
        model = Sepet

class OnayAdmin(admin.ModelAdmin):
    list_display = ('sepet', 'adet', 'depo', 'eklenme', 'duzenlenme', 'id', )
    list_per_page = 20
    list_filter = ('sepet', 'depo', )
    class Meta:
        model = SepetOnay

admin.site.register(Stok, StokAdmin)
admin.site.register(Sepet, SepetAdmin)
admin.site.register(SepetOnay, OnayAdmin)