from django.urls import path
from . import views

app_name = 'ilaclar'

urlpatterns = [
    path('ilaclar', views.IlacList.as_view(), name='ilac-list'),
    # path('ilac/<ilac_adi>/', views.IlacMustahzarList.as_view(), name='ilac-detay'),
    path('etkenmadde/', views.EtkenMaddeList.as_view(), name='etkenmadde-list'),
]