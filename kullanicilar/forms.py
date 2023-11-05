from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Kullanici

class KullaniciOlusturForm(UserCreationForm):

    class Meta:
        model = Kullanici
        fields = ('gln', 'username', 'email', 'sehir', 'sirket_tipi', 'sirket_adi', )

class KullaniciDegistirForm(UserChangeForm):

    class Meta:
        model = Kullanici
        fields = ('username', 'email', 'sehir', 'sirket_tipi', 'sirket_adi', )