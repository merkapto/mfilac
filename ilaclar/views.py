from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Ilac, EtkenMadde

class IlacList(ListView):
    model = Ilac
    context_object_name = 'ilac_listesi'

class EtkenMaddeList(ListView):
    model = EtkenMadde
    context_object_name = 'etkenmadde_listesi'