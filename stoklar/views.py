from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Stok, Sepet, SepetOnay
from kullanicilar.models import Kullanici


# ---------------------------------------------------------------------------------
# STOK BÖLÜMÜ

class StokList(ListView):
    def get_queryset(self):
        return Stok.objects.filter(depo__sehir=self.request.user.sehir)  # .order_by('-duzenlenme')


class BenimStokList(ListView):
    template_name = 'stoklar/stoklarim.html'

    def get_queryset(self):
        return Stok.objects.filter(depo=self.request.user).order_by('ilac')


class StokCreate(CreateView):
    model = Stok
    fields = ['ilac', 'adet']
    success_url = reverse_lazy('stoklar:benim-stok-list')

    def form_valid(self, form):
        form.instance.depo = self.request.user
        form.instance.kalan = form.instance.adet
        return super().form_valid(form)


class StokUpdate(UpdateView):
    model = Stok
    fields = ['ilac', 'adet']
    template_name = 'stoklar/stok_form.html'


class StokDelete(DeleteView):
    model = Stok
    success_url = reverse_lazy('stoklar:benim-stok-list')

    def get(self, *args, **kwargs):
        return self.delete(*args, **kwargs)


# -----------------------------------------------------------------------
# SEPET BÖLÜMÜ

class BenimSepetList(ListView):
    template_name = 'stoklar/sepetim.html'

    def get_queryset(self):
        return Sepet.objects.filter(eczane=self.request.user).order_by('-duzenlenme')


class SepetCreate(CreateView):
    model = Sepet
    fields = ['adet', ]

    def dispatch(self, request, *args, **kwargs):
        self.stok = get_object_or_404(Stok, pk=kwargs['pk'])
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.eczane = self.request.user
        form.instance.stok = self.stok

        return super().form_valid(form)


class SepetUpdate(UpdateView):
    model = Sepet
    fields = ['stok', 'adet']
    template_name = 'stoklar/sepet_form.html'


class SepetDelete(DeleteView):
    model = Sepet
    success_url = reverse_lazy('stoklar:benim-sepet-list')

    def get(self, *args, **kwargs):
        return self.delete(*args, **kwargs)


# -----------------------------------------------------------------------
# ONAY BÖLÜMÜ

class BenimOnayList(ListView):
    template_name = 'stoklar/onaylarim.html'

    def get_queryset(self):
        return SepetOnay.objects.filter(sepet__stok__depo=self.request.user)


class OnayCreate(CreateView):
    model = SepetOnay
    fields = ['adet', 'onay']

    def dispatch(self, request, *args, **kwargs):
        self.sepet = get_object_or_404(Sepet, pk=kwargs['pk'])
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form, **kwargs):
        form.instance.depo = self.request.user
        form.instance.sepet = self.sepet
        # self.sepet.stok.kalan -= form.instance.adet
        return super().form_valid(form)

    # def save(self):
    #     self.sepet.stok.kalan = self.sepet.stok.kalan - self.adet
    #     return self.sepet.stok.kalan

class OnayUpdate(UpdateView):
    model = SepetOnay
    fields = ['adet', 'onay']
    template_name = 'stoklar/onay_form.html'