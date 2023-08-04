from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('hash_algorithm/', views.hash_algorithm, name = 'hash_algorithm'),
    path('rsa_generator/', views.rsa_generator, name = 'rsa_generator'),
    path('all_keys/', views.all_keys, name = 'all_keys'),
    path('certification/', views.certification, name='certificate_generator'),
    path('all_certificates/', views.all_certificates, name='all_certificates')
]
