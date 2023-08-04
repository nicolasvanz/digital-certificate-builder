from datetime import datetime, timedelta
from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.serialization import KeySerializationEncryption, load_pem_public_key, load_pem_private_key

def generate_cert(name, ca_key, public_key, self_signed = False, ca_name = None):
    subject = issuer =  x509.Name([x509.NameAttribute(NameOID.COMMON_NAME, name)])
    if not self_signed:
        issuer  = x509.Name([x509.NameAttribute(NameOID.COMMON_NAME, ca_name)])
    snumber = x509.random_serial_number()
    now = datetime.now()
    cert = (
        x509.CertificateBuilder()
        .subject_name(subject)
        .issuer_name(issuer)
        .public_key(load_pem_public_key(str.encode(public_key), backend=default_backend()))
        .serial_number(snumber)
        .not_valid_before(now)
        .not_valid_after(now + timedelta(days=10*365))
        .sign(load_pem_private_key(str.encode(ca_key), backend = default_backend(), password = None), hashes.SHA256(), default_backend())
    )
    cert_pem = cert.public_bytes(encoding=serialization.Encoding.PEM)
    return [cert_pem, snumber]
