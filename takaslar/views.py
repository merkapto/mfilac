from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
# from django import forms

from .models import Takas, Talep, Onay
# from .forms import TalepCreateForm
from kullanicilar.models import Kullanici


# ---------------------------------------------------------------------------------
# TAKAS BÖLÜMÜ

class TakasList(ListView):
    def get_queryset(self):
        return Takas.objects.exclude(takas_veren=self.request.user).filter(
            takas_veren__sehir=self.request.user.sehir)#.order_by('-eklenme')


class BenimTakasList(ListView):
    template_name = 'takaslar/takaslarim.html'

    def get_queryset(self):
        return Takas.objects.filter(takas_veren=self.request.user)#.order_by('-eklenme')

class BenimTakasDetail(DetailView):
    model = Takas

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class TakasCreate(CreateView):
    model = Takas
    fields = ['ilac', 'adet', 'miad']

    def form_valid(self, form):
        form.instance.takas_veren = self.request.user
        return super().form_valid(form)


class TakasUpdate(UpdateView):
    model = Takas
    fields = ['ilac', 'adet']
    template_name = 'takaslar/takas_form.html'


class TakasDelete(DeleteView):
    model = Takas
    success_url = reverse_lazy('takaslar:benim-takas-list')

    def get(self, *args, **kwargs):
        return self.delete(*args, **kwargs)


# -----------------------------------------------------------------------
# TALEP BÖLÜMÜ

class BenimTalepList(ListView):
    template_name = 'takaslar/taleplerim.html'

    def get_queryset(self):
        return Talep.objects.filter(talep_eden=self.request.user)#.order_by('-eklenme')


class TalepCreate(CreateView):
    model = Talep
    fields = ['adet']

    def dispatch(self, request, *args, **kwargs):
        self.takas = get_object_or_404(Takas, pk=kwargs['pk'])
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.talep_eden = self.request.user
        form.instance.takas = self.takas
        return super().form_valid(form)


class TalepUpdate(UpdateView):
    model = Talep
    fields = ['takas', 'adet', 'mesaj']
    template_name = 'takaslar/talep_form.html'


class TalepDelete(DeleteView):
    model = Talep
    success_url = reverse_lazy('takaslar:benim-talep-list')

    def get(self, *args, **kwargs):
        return self.delete(*args, **kwargs)


# -----------------------------------------------------------------------
# ONAY BÖLÜMÜ

class BenimOnayList(ListView):
    template_name = 'takaslar/onaylarim.html'

    def get_queryset(self):
        return Onay.objects.filter(talep__takas__takas_veren=self.request.user)


class OnayCreate(CreateView):
    model = Onay
    fields = ['adet', 'onay']

    def dispatch(self, request, *args, **kwargs):
        self.talep = get_object_or_404(Talep, pk=kwargs['pk'])
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form, **kwargs):
        form.instance.onay_veren = self.request.user
        form.instance.talep = self.talep
        return super().form_valid(form)


class OnayUpdate(UpdateView):
    model = Onay
    fields = ['adet', 'mesaj', 'onay']
    template_name = 'takaslar/onay_form.html'