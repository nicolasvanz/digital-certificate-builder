from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend

def generate_RSA(bits):
    key = rsa.generate_private_key(
        public_exponent = 65537,
        key_size = bits,
        backend = default_backend()
    )
    return key
