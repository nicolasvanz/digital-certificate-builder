from django.shortcuts import render, get_object_or_404
from scripts.take_hash import hash_string
from scripts.generate_rsa_keys import generate_RSA
from scripts.certification import generate_cert
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from .models import Keypair, CertificateAutority, Certificate


def index(request):
    return render(request, 'main.html')

def hash_algorithm(request):
    if request.method == "POST":
        try:
            uploaded_file = request.FILES['document']
            file_hash = hash_string(uploaded_file)
            return render(request, 'hash_algorithm.html', {'hash' : file_hash})
        except:
            pass
    return render(request, 'hash_algorithm.html')

def rsa_generator(request):
    if request.method == 'POST' and ('bits' in request.POST.keys()):
        bits_value = request.POST['bits']
        key = generate_RSA(int(bits_value))
        pvk = key.private_bytes(encoding=serialization.Encoding.PEM,
                                format=serialization.PrivateFormat.TraditionalOpenSSL,
                                encryption_algorithm=serialization.NoEncryption()).decode('ascii')
        pbk = key.public_key().public_bytes(encoding=serialization.Encoding.PEM,
                                            format=serialization.PublicFormat.SubjectPublicKeyInfo).decode('ascii')
        keypair = Keypair(len(Keypair.objects.all()) + 1, len(Keypair.objects.all()) + 1, int(bits_value), pbk, pvk)
        keypair.save()
        return render(request, 'rsa_generator.html', {'private_key' : pvk,'public_key' : pbk})
    return render (request, 'rsa_generator.html')

def certification(request):
    if request.method == 'POST':
        if 'name' in request.POST.keys() and 'key' in request.POST.keys():
            selected_key = get_object_or_404(Keypair, pk = request.POST['key'])
            certificate_autority = CertificateAutority(len(CertificateAutority.objects.all()) + 1, len(CertificateAutority.objects.all()) + 1, selected_key.private_key, selected_key.public_key, request.POST['name'])
            certificate_autority.save()
        elif 'CA-selfSign' in request.POST.keys():
            selected_ca = get_object_or_404(CertificateAutority, pk = request.POST['CA-selfSign'])
            c = generate_cert(selected_ca.name, selected_ca.private_key, selected_ca.public_key, self_signed = True)
            certificate = Certificate(len(Certificate.objects.all()) + 1, len(Certificate.objects.all()) + 1, selected_ca.name, c[1], selected_ca.name, c[0].decode('ascii'))
            certificate.save()
            return render(request, 'certification.html', {'key_list' : Keypair.objects.all(), 'self_signed_certificate' : c[0].decode('ascii'), 'ca_list' : CertificateAutority.objects.all()})
        elif 'CA-signed' in request.POST.keys():
            selected_ca = get_object_or_404(CertificateAutority, pk = request.POST['CA-signed'])
            selected_key = get_object_or_404(Keypair, pk = request.POST['key'])
            c = generate_cert(request.POST['subject'], selected_ca.private_key, selected_key.public_key, ca_name = selected_ca.name)
            certificate = Certificate(len(Certificate.objects.all()) + 1, len(Certificate.objects.all()) + 1, request.POST['subject'], c[1], selected_ca.name, c[0].decode('ascii'))
            certificate.save()
            return render(request, 'certification.html', {'key_list' : Keypair.objects.all(), 'signed_certificate' : c[0].decode('ascii'), 'ca_list' : CertificateAutority.objects.all()})
    return render(request, 'certification.html', {'key_list' : Keypair.objects.all(), 'ca_list' : CertificateAutority.objects.all()})

def all_certificates (request):
    return render(request, 'all_certificates.html', {'certificates_list' : Certificate.objects.all()})
    
def all_keys(request):
    return render(request, 'all_keys.html', {'keys_list' : Keypair.objects.all()})
