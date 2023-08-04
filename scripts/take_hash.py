import hashlib

def hash_string(file):
    return hashlib.sha256(file.read()).hexdigest()
