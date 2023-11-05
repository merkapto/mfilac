from django.urls import path
from . import views

app_name = 'stoklar'

urlpatterns = [
    path('stokliste/', views.StokList.as_view(), name='stok-list'),

    path('stoklarim/', views.BenimStokList.as_view(), name='benim-stok-list'),
    path('stok/ekle/', views.StokCreate.as_view(), name='stok-ekle'),
    path('stok/<int:pk>/', views.StokUpdate.as_view(), name='stok-guncelle'),
    path('stok/<int:pk>/sil/', views.StokDelete.as_view(), name='stok-sil'),

    path('sepetim/', views.BenimSepetList.as_view(), name='benim-sepet-list'),
    path('sepet/ekle/<int:pk>/', views.SepetCreate.as_view(), name='sepet-ekle'),
    path('sepet/<int:pk>/', views.SepetUpdate.as_view(), name='sepet-guncelle'),
    path('sepet/<int:pk>/sil/', views.SepetDelete.as_view(), name='sepet-sil'),

    path('onaylarim/', views.BenimOnayList.as_view(), name='benim-onay-list'),
    path('onay/ekle/<int:pk>', views.OnayCreate.as_view(), name='onay-ekle'),
    path('onay/<int:pk>/', views.OnayUpdate.as_view(), name='onay-guncelle'),
]