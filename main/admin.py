from django.contrib import admin

from .models import Keypair, Certificate, CertificateAutority

admin.site.register(Keypair)
admin.site.register(Certificate)
admin.site.register(CertificateAutority)

# Register your models here.
