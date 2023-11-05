from django.contrib import admin

from .models import Takas, Talep, Onay


class TakasAdmin(admin.ModelAdmin):
    list_display = ('ilac', 'adet', 'kalan', 'miad', 'takas_veren', 'eklenme', 'duzenlenme', 'id', 'ilac_id')
    list_per_page = 20
    list_filter = ('ilac', 'takas_veren',)
    search_fields = ['ilac']

    class Meta:
        model = Takas


class TalepAdmin(admin.ModelAdmin):
    list_display = ('takas', 'adet', 'onay_durum', 'talep_eden', 'takas_veren', 'eklenme', 'duzenlenme', 'id', 'takas_id')
    list_per_page = 20
    list_filter = ('takas', 'talep_eden', )
    search_fields = ['takas']

    class Meta:
        model = Talep


class OnayAdmin(admin.ModelAdmin):
    list_display = ('talep', 'adet', 'onay', 'onay_veren', 'talep_eden', 'takas_veren', 'id', 'talep_id')
    list_per_page = 20
    list_filter = ('onay', 'onay_veren',)
    search_fields = ['talep']

    class Meta:
        model = Onay


admin.site.register(Takas, TakasAdmin)
admin.site.register(Talep, TalepAdmin)
admin.site.register(Onay, OnayAdmin)
