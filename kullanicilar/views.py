from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import KullaniciOlusturForm

class SignUpView(CreateView):
    form_class = KullaniciOlusturForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'