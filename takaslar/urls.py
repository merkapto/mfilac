from django.urls import path
from . import views

app_name = 'takaslar'
urlpatterns = [
    path('takasliste/', views.TakasList.as_view(), name='takas-list'),

    path('takaslarim/', views.BenimTakasList.as_view(), name='benim-takas-list'),
    path('takaslarim/<int:pk>/', views.BenimTakasDetail.as_view(), name='benim-takas-detay'),
    path('takas/ekle/', views.TakasCreate.as_view(), name='takas-ekle'),
    path('takas/<int:pk>/', views.TakasUpdate.as_view(), name='takas-guncelle'),
    path('takas/<int:pk>/sil/', views.TakasDelete.as_view(), name='takas-sil'),

    path('taleplerim/', views.BenimTalepList.as_view(), name='benim-talep-list'),
    path('talep/ekle/<int:pk>/', views.TalepCreate.as_view(), name='talep-ekle'),
    path('talep/<int:pk>/', views.TalepUpdate.as_view(), name='talep-guncelle'),
    path('talep/<int:pk>/sil/', views.TalepDelete.as_view(), name='talep-sil'),

    path('onaylarim/', views.BenimOnayList.as_view(), name='benim-onay-list'),
    path('onay/ekle/<int:pk>', views.OnayCreate.as_view(), name='onay-ekle'),
    path('onay/<int:pk>/', views.OnayUpdate.as_view(), name='onay-guncelle'),
]