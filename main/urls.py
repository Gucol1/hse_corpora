from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('peclap_info', views.peclap_info, name='peclap_info'),
    path('peclap_word', views.peclap_word, name='peclap_word'),
    path('peclap_kwic', views.peclap_kwic, name='peclap_kwic'),
]