from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import KullaniciOlusturForm, KullaniciDegistirForm
from .models import Kullanici

class KullaniciAdmin(UserAdmin):
    add_form = KullaniciOlusturForm
    form = KullaniciDegistirForm
    model = Kullanici
    search_fields = ('username', 'sirket_adi', 'email', )
    list_per_page = 20
    list_display = ('username', 'sirket_adi', 'sirket_tipi', 'sehir', 'email', )
    list_filter = ('sehir', 'sirket_tipi', )

    fieldsets = (
        ('Bilgiler', {'fields': ('gln', 'sirket_adi', 'sirket_tipi', 'sehir', 'cep_telefon', 'is_telefon', 'adres')}),
    ) + UserAdmin.fieldsets 
    # fieldsets = (
    #     (None, {'fields': ('username', 'password', 'sirket_adi', 'sirket', 'sehir', 'email')}),
    #     ('Bilgiler', {'fields': ('cep_telefon', 'is_telefon', 'adres')})
    # )

admin.site.register(Kullanici, KullaniciAdmin)
