from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('peclap_info', views.peclap_info, name='peclap_info'),
    path('peclap_word', views.peclap_word, name='peclap_word'),
    path('peclap_kwic', views.peclap_kwic, name='peclap_kwic'),
    path('peclap_ngram', views.peclap_ngram, name='peclap_ngram'),
    path('pecase_info', views.pecase_info, name='pecase_info'),
    path('pecase_word', views.pecase_word, name='pecase_word'),
    path('pecase_kwic', views.pecase_kwic, name='pecase_kwic'),
    path('pecase_ngram', views.pecase_ngram, name='pecase_ngram'),
]