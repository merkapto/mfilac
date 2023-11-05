from django.contrib import admin

from .models import Ilac, EtkenMadde

class EtkenMaddeAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'id')
    class Meta:
        model = EtkenMadde
        
# class EtkenMaddeInline(admin.TabularInline):
#     model = EtkenMadde
#     extra = 1

class IlacAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'get_etkenmadde', 'resim', 'aktif', 'id', )
    # inlines = [EtkenMaddeInline, ]
    class Meta:
        model = Ilac


admin.site.register(Ilac, IlacAdmin)
admin.site.register(EtkenMadde, EtkenMaddeAdmin)